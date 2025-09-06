from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


model = ChatGoogleGenerativeAI(model= 'gemini-2.5-pro')

#prompt1
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)

#prompt2
template2 = PromptTemplate(
    template='Write a 5 line summary of following text. /n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser
result = chain.invoke({'topic':'Black Hole'})

print(result)