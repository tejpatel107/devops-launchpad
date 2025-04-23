import streamlit as st
import requests
import os

# Set up Streamlit page
st.set_page_config(page_title="Easy Chatbot", page_icon="🤖")

# Define the Docker Model Runner backend URL
docker_ip = os.getenv("DOCKER_IP", "localhost")
DOCKER_API_URL = f"http://{docker_ip}:12434/engines/llama.cpp/v1/chat/completions"  # Replace with your actual Docker model runner endpoint

# Streamlit UI
st.title("💬 Your Own Chatbot 💬")
st.write("This is a simple chatbot using Streamlit for UI and Docker Model Runner for backend.")

# Create a text input for user to type a message
user_message = st.text_input("You: ", "")

# Maintain chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Function to send message to Docker Model Runner backend and parse response
def get_docker_response(message):
    # Define the payload for Docker Model Runner API
    payload = {
        "model": "ai/qwen2.5",  # Replace with your specific model if needed
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ]
    }
    
    try:
        # Send POST request to the Docker Model Runner API
        print("Firing request to ", DOCKER_API_URL)
        response = requests.post(DOCKER_API_URL, json=payload)
        
        if response.status_code == 200:
            # Extract the assistant's response from the JSON structure
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"Error: {response.status_code}, {response.text}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"

# Clear previous chat history when a new message is entered
if user_message:
    # Reset chat history for each new message
    st.session_state.chat_history = [{"role": "user", "content": user_message}]

    # Get response from Docker Model Runner
    bot_response = get_docker_response(user_message)
    
    # Add bot response to chat history
    st.session_state.chat_history.append({"role": "bot", "content": bot_response})

# Display chat history
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(f"**You:** {chat['content']}")
    else:
        st.markdown(f"**Bot:** {chat['content']}")
