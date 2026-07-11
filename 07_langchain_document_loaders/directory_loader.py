from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from pathlib import Path

dict_path = (
    Path(__file__).parent
    / "books"
)

loader = DirectoryLoader(
    path=dict_path,
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

# loads all documents simeltanously in memory
# docs = loader.load() 

docs = loader.lazy_load() # load only one document at a time in memory

for doc in docs:
    print(doc.page_content)