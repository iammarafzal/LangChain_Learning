from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

file_path = (
    Path(__file__).parent
    / "books"
    / "Building Machine Learning Systems with Python - Second Edition.pdf"
)

loader = PyPDFLoader(file_path=file_path)

docs = loader.load()

print(docs[10].page_content)
print(len(docs))
