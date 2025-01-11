from flask import Flask, request, jsonify, render_template, session
import subprocess
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'flaskkey' 

def format_conversation(conversation):
    formatted_prompt = ""
    for msg in conversation:
        role = msg['role']
        content = msg['content']
        formatted_prompt += f"{role}: {content}\n"
    return formatted_prompt

def generate_response(prompt, conversation_history):
    try:
        # Add the new user message to conversation history
        conversation_history.append({
            'role': 'user',
            'content': prompt,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        # Format the entire conversation for the model
        full_context = format_conversation(conversation_history)
        
        command = ['ollama', 'run', 'hf.co/praneethposina/customer_support_bot:Q4_K_M', full_context]
        print(f"Running command: {' '.join(command)}")  
        
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',
            check=True
        )
        
        output = result.stdout.strip()
        filtered_output = "\n".join(
            line for line in output.splitlines()
            if "failed to get console mode" not in line
        )
        
        # Add the assistant's response to conversation history
        conversation_history.append({
            'role': 'assistant',
            'content': filtered_output,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        return filtered_output
        
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e.stderr.strip()}")
        return f"Error: {e.stderr.strip()}"

@app.route('/')
def index():
    # Initialize empty conversation history when starting new session
    if 'conversation_history' not in session:
        session['conversation_history'] = []
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data.get('prompt', '')
    
    # Get conversation history from session or initialize if not exists
    conversation_history = session.get('conversation_history', [])
    
    response = generate_response(prompt, conversation_history)
    
    # Update session with new conversation history
    session['conversation_history'] = conversation_history
    
    return jsonify({
        'response': response,
        'conversation_history': conversation_history
    })

@app.route('/clear', methods=['POST'])
def clear_history():
    # Clear the conversation history
    session['conversation_history'] = []
    return jsonify({'message': 'Conversation history cleared'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port, debug=False)
