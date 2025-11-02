from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatGoogleGenerativeAI(model = 'gemini-2.5-pro')

prompt1 = PromptTemplate(
    template = 'Generate a short and simple notes from the following text \n {text}',
    input_variables=['text'] 
)

prompt2 = PromptTemplate(
    template = 'Geenrate 5 short  question answers from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template = 'Merge the provided notes and quiz intoo a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes','quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model1 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """A Support Vector Machine (SVM) is a supervised machine learning algorithm used for both classification and regression, though it is mainly applied to classification tasks. 
          The main goal of SVM is to find an optimal hyperplane that separates data points belonging to different classes with the maximum possible margin. 
          The data points that lie closest to this decision boundary are called support vectors, and they play a crucial role in defining the position and orientation of the hyperplane. 
          SVM performs exceptionally well in high-dimensional spaces and is effective even when the number of features exceeds the number of samples. 
          To handle nonlinear data, SVM uses the kernel trick, which transforms data into a higher-dimensional space to make it linearly separable. 
          Common kernel functions include linear, polynomial, and radial basis function (RBF). SVM also includes a regularization parameter (C) that controls the trade-off between maximizing the margin and minimizing classification error. 
          While SVMs provide strong generalization and robustness to overfitting, they can be computationally expensive for large datasets and sensitive to kernel and parameter selection. 
          Despite these challenges, SVMs are widely used in fields such as text categorization, image recognition, and bioinformatics due to their accuracy and versatility."""

result = chain.invoke({'text':text})

print(result)

chain.get_graph().print_ascii()