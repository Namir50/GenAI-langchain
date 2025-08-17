from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-pro')

chathistory = [
    SystemMessage(content='You are a helpful assistant' ),
]

while True:
    user = input("You: ")
    chathistory.append(HumanMessage(content=user))
    if user == 'exit':
        break
    result = model.invoke(chathistory)
    print(f"AI: {result.content}")
    chathistory.append(AIMessage(content=result.content))