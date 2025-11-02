from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-pro')

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into positive or negative \n {feedback}',
    input_variables=['feedback']
)

classifier_chain = prompt1 | model | parser

result = classifier_chain.invoke({'feedback':'This is a terrible smartphone'})

print(result)