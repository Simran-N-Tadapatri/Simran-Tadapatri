from ollama import Client

# 1. Initialize the Ollama client
client = Client(host="http://localhost:11434")

# 2. Store the conversation history
messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful AI assistant. "
            "Keep your answers simple, clear, and informative. "
            "Do not use bullet points or numbering."
        )
    }
]

print("Welcome to Ollama AI Chatbot!")
print("Type 'exit' to stop chatting.\n")