document.addEventListener('DOMContentLoaded', (event) => {
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');

    userInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            sendMessage();
        }
    });

    sendButton.addEventListener('click', sendMessage);
});

function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (!userInput.trim()) return;

    const messages = document.getElementById('messages');
    messages.innerHTML += `<div class="message user-message">User: ${userInput}</div>`;
    document.getElementById('user-input').value = '';

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ prompt: userInput })
    })
    .then(response => response.json())
    .then(data => {
        messages.innerHTML += `<div class="message bot-message">Bot: ${data.response}</div>`;
        messages.scrollTop = messages.scrollHeight;
    });
}
