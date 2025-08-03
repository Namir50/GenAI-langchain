from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-pro')
#Here too you can use parameters

result = model.invoke("What is capital of India")

print(result)
print(result.content)