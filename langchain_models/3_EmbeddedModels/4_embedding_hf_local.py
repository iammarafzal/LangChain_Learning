from langchain_huggingface import HuggingFaceEmbeddings

import os
# Make sure to set HF_TOKEN in your environment variables
# os.environ["HF_TOKEN"] = "your_huggingface_token"


embedding = HuggingFaceEmbeddings(
    model_name='sentence-transformers/all-MiniLM-L6-v2',
    cache_folder=r"D:\HuggingFace\huggingface_cache\hub"
)

documents = [
    "The cat is sleeping on the sofa.",
    "A kitten is taking a nap on the couch.",
    "Dogs are loyal and friendly pets.",
    "Python is a programming language used for AI.",
    "Large language models can generate human-like text."
]

vectors = embedding.embed_documents(documents)

print(len(vectors[0]))