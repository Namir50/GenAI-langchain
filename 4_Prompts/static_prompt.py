from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("Research tool")

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

user_input = st.text_input('Enter your prompt')

if st.button('Summarize'):
    result = model.invoke('User input')
    st.write(result.content)
