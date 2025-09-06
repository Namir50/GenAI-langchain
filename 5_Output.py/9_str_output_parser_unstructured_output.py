from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation"
)
model = ChatHuggingFace(llm = llm)

#prompt1
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)

#prompt2
template1 = PromptTemplate(
    template='Write a 5 line summary of following text. /n {text}',
    input_variables=['text']
)