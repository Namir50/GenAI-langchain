from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-pro')

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment : Literal['positive','negative'] = Field(description='Give the sentiment of the following feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

print(classifier_chain.invoke({'feedback':'This is a terrible phone'}).sentiment)

prompt2 = PromptTemplate(
    template = 'You are a customer support agent. for this positive feedback, write a short, polite, empathetic response (2–3 sentences) \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template = 'You are a customer support agent. for this negative feedback, write a short, polite, empathetic response (2–3 sentences) \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: 'Could not find the sentiment')
)

chain = classifier_chain | branch_chain

result = chain.invoke({'feedback':'This is a wonderful phone which i purchased'})

print(result)