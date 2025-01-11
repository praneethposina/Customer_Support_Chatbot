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
[Insert chatbot interface screenshot]

### AWS CloudWatch Monitoring
[Insert CloudWatch monitoring screenshot]

### Docker Logs
[Insert Docker logs screenshot]


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

