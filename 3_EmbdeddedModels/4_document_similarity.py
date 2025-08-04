from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(
    model = 'text-embedding-3-large',
    dimensions=300
)

document = [
    "Virat Kohli is known for his aggressive batting style and is one of India's most successful and consistent run-scorers in all formats.",
    "Rohit Sharma, the current captain of the Indian team, holds the record for the highest individual score in a One Day International (264 runs)."
    "Jasprit Bumrah is India's premier fast bowler, famous for his deadly yorkers and unorthodox bowling action."
    "Ravindra Jadeja is a dynamic all-rounder who contributes with explosive batting, accurate spin bowling, and sharp fielding."
    "Shubman Gill is a rising star in Indian cricket, praised for his elegant stroke play and calm temperament at the crease."
]

query = "tell me about virat kohli"

doc_embeddings = embedding.embed_documents(document)
query_embeddings = embedding.embed_query(query)

cosine_similarity([query_embeddings], doc_embeddings)
#here we have to send query in 2 dimension, document is already in 2 dimension 
scores = cosine_similarity([query_embeddings],doc_embeddings)[0]

index, score = (sorted(list(enumerate(scores)),key=lambda x:x[1])[-1])

print(query)
print(document[index])
print("similarity score is:",score)