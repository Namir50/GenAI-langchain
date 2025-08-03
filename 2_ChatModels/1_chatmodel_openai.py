from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4',temperature=0.5, max_completion_tokens=10)
#temperature is a paramter that controls the randomness of a language model's output, it affects how creative or deterministic the response will be, range 0 to 2
#max_completion_tokens is used to set number of tokens in the response

result = model.invoke("What is the capital of India?")

print(result)
print(result.content)

