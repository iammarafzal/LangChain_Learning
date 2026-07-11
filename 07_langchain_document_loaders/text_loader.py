from langchain_community.document_loaders import TextLoader
from pathlib import Path
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Write a short summary of the given poem \n {poem}',
    input_variables=['poem']
)

file_path = Path(__file__).with_name("cricket.txt")
loader = TextLoader(file_path, encoding="utf-8")

docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({'poem': docs})

print(result)