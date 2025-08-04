from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions=32)  
#In embedding models, "dimension" refers to the number of features (or numerical values) used to represent a single item (like a word, sentence, document, image, etc.) in vector space
#Higher dimensions can capture more complex relationships (like context, sentiment, semantics).

documents = [
    "This is a sample document.",
    "This is another sample document.",
    "This is a third sample document."
]
vector = embedding.embed_documents(documents)

print(str(vector))