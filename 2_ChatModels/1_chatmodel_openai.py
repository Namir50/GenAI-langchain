from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4',temperature=0.5)
#temperature is a paramter that controls the randomness of a language model's output, it affects how creative or deterministic the response will be, range 0 to 2

result = model.invoke("What is the capital of India?")

print(result)
print(result.content)

