from langchain_classic.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

file_path = (Path(__file__).cwd()
    / "07_langchain_document_loaders"
    / "books"
    / "Building Machine Learning Systems with Python - Second Edition.pdf"
)

loader = PyPDFLoader(file_path=file_path)

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_documents(docs)

print(result[1].page_content)