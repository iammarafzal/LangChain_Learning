from langchain_community.document_loaders import CSVLoader
from pathlib import Path

file_path = Path(__file__).with_name('Social_Network_Ads.csv')
loader = CSVLoader(file_path=file_path)

docs = loader.load()

print(len(docs))