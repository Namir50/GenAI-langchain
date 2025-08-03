from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='Claude-3-5-sonnet-20241022')
#here too we can set parameters

result = model.invoke("What is the capital of india")

print(result)
print(result.content)