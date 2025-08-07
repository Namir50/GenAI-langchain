from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv

model = ChatOpenAI(model = 'gpt-3.5-turbo', temperature = 0.5)

st.header = ('Research Tool')

paper_input = st.selectbox("Select Research paper name", ['Select..','Attention is all you need',
                                                          'BERT: Pre-training of deep bidirectional transformer',
                                                          'GPT-3: Language models are few shot learners',
                                                          'Diffusion models beat GANs on image synthesis'])

style_input = st.selectbox("Seelct explanation style",['Beginner friendly',
                                                       'Techical',
                                                       'Code-oriented',
                                                       'Mathematical'])

length_input = st.selectbox('Select explanation length',['Short',
                                                         'Medium',
                                                         'Long'])


template = PromptTemplate(
    input_variables=['paper_inout','style_input','length_input']  
)

prompt = template.invoke({
    'paper_input' : paper_input,
    'style_input' : style_input,
    'length_input': length_input
})

if st.button("Summarize"):
    result = model.invoke(prompt)
    st.write(result.content)