from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(
    model='text-embedding-3-large',
    dimensions=300
    )

documents = [
    "The cat is sleeping on the sofa.",
    "A kitten is taking a nap on the couch.",
    "Dogs are loyal and friendly pets.",
    "Python is a programming language used for AI.",
    "Large language models can generate human-like text."
]

query = ""

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)

index, score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("Similarity Score is: ", score)