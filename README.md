# Customer Support Chatbot with LLaMA 3.1

> An end-to-end customer support chatbot solution powered by fine-tuned LLaMA 3.1 8B model, deployed using Flask, Docker, and AWS ECS.

## Overview

This project implements a sophisticated customer support chatbot leveraging the LLaMA 3.1 8B model fine-tuned on customer support conversations. The solution uses LoRA fine-tuning and various quantization techniques for optimized inference, deployed as a containerized application on AWS ECS with Fargate.

## Features

- **Fine-tuned LLaMA 3.1 Model**: Customized for customer support using the [Bitext customer support dataset](https://huggingface.co/datasets/bitext/Bitext-customer-support-llm-chatbot-training-dataset)
- **Optimized Inference**: Implements 4-bit, 8-bit, and 16-bit quantization
- **Containerized Deployment**: Docker-based deployment for consistency and scalability
- **Cloud Infrastructure**: Hosted on AWS ECS with Fargate for serverless container management
- **CI/CD Pipeline**: Automated deployment using AWS CodePipeline
- **Monitoring**: Comprehensive logging and monitoring via AWS CloudWatch

## Model Details

The fine-tuned model is hosted on Hugging Face:
- Model Repository: [praneethposina/customer_support_bot](https://huggingface.co/praneethposina/customer_support_bot)
- Base Model: LLaMA 3.1 8B
- Training Dataset: Bitext Customer Support Dataset
- Optimization: LoRA fine-tuning with quantization

## Tech Stack

- **Backend**: Flask API
- **Model Serving**: Ollama
- **Containerization**: Docker
- **Cloud Services**: 
  - AWS ECS (Fargate)
  - AWS CodePipeline
  - AWS CloudWatch
- **Model Training**: LoRA, Quantization

## Screenshots

### Chatbot Interface

![Chatbot SS](https://github.com/user-attachments/assets/220aea77-bb2b-4f50-b6a4-0541434d85ef)

![Chatbot SS2](https://github.com/user-attachments/assets/da440735-59d7-4be7-a43d-d51de8983738)

### AWS CloudWatch Monitoring

![CloudWatch SS](https://github.com/user-attachments/assets/9794bc3e-4b9c-4626-9a7f-3936d4757328)

### Docker Logs

<img width="1270" alt="Docker ss" src="https://github.com/user-attachments/assets/a72d1c35-8203-4a05-b944-743ea6c0a6b8" />
<img width="1268" alt="Docker ss2" src="https://github.com/user-attachments/assets/f1b0c0b1-2aad-462c-adf2-7a7ea9047a1a" />

## AWS Deployment

1. Push Docker image to Amazon ECR
2. Configure AWS ECS Task Definition
3. Set up AWS CodePipeline for CI/CD
4. Configure CloudWatch monitoring


## Project Structure
```
├── app.py                  # Flask application
├── static/                 # Static files
│   ├── script.js          # Frontend JavaScript
│   └── styles.css         # CSS styles
├── templates/             # HTML templates
├── Dockerfile             # Docker configuration
├── requirements.txt       # Python dependencies
├── Customer_support_bot.ipynb       # Model Fine-tuning using unsloth
└── supervisord.conf       # Supervisor configuration
```

