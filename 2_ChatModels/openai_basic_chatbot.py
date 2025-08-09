from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai_api = os.getenv("OPENAI_API_KEY")
print("API Key loaded:", openai_api is not None)  # Check if key loaded

model = ChatOpenAI(
    model="gpt-5",
    api_key= openai_api,
    temperature=0.7
)

chat_history = [] #for maintaining memory and history
while True:
    user_input = input("You: ")
    chat_history.append(user_input)  
    if user_input.lower() == 'exit':
        break
    result = model.invoke(chat_history)  #invoke function is flexible enough too take single message as well as list of messages
    chat_history.append(result.content)  #also appending the bot's response to the chat history
    print("AI:", result.content)  
