Here's the content converted into a **README.md** format with just the commands:


# Docker Model Runner for LLM Apps on Laptop

This guide explains how to set up **Docker Model Runner** on your laptop for **LLM (Large Language Model)** inferencing, and how to deploy a **chatbot** interface using **Streamlit**.

## Prerequisites

- **Docker** installed on your laptop.
- **Streamlit** installed on your laptop.

## Steps to Set Up Docker Model Runner and Test LLM Inferencing

### 1. Install Docker and Enable Docker Model Runner

```bash
# Enable Docker Model Runner
docker desktop enable model-runner

# Enable TCP connection on port 12434
docker desktop enable model-runner --tcp 12434
```

### 2. Choose a Model Based on Your System Configuration

```bash
# Remove a model if necessary
docker model rm ai/qwen2.5
```

### 3. Verify Access to Docker Model Runner from Host Machine

```bash
# Verify Docker Model Runner is accessible
curl http://model-runner.docker.internal/engines/llama.cpp/v1
```

You should see:

```
Docker Model Runner
The service is running.
```

### 4. Test Full LLM Inferencing Command

```bash
curl http://localhost:12434/engines/llama.cpp/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "ai/qwen2.5",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Please write 500 words about the fall of Rome."
            }
        ]
    }'
```

### 5. Test from Another Container (Optional)

```bash
curl http://model-runner.docker.internal/engines/llama.cpp/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "ai/qwen2.5",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Please write 500 words about the fall of Rome."
            }
        ]
    }'
```

### 6. Install Streamlit and Launch Your Chatbot

```bash
# Install Streamlit
pip install streamlit
```

### 7. Run the Chatbot App

```bash
# Run the chatbot Streamlit app
streamlit run Chatbot.py
```

Your chatbot should now be available at:

```
Local URL: http://localhost:8501
Network URL: http://<your-ip>:8501
```

