from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "The cat is sleeping on the sofa.",
    "A kitten is taking a nap on the couch.",
    "Dogs are loyal and friendly pets.",
    "Python is a programming language used for AI.",
    "Large language models can generate human-like text."
]

vectors = model.embed_documents(documents)

print(str(vectors))