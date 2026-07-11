import os
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question', 'text']
)

parser = StrOutputParser()

url = "https://www.junaidjamshed.com/pages/returns-exchanges"

loader = WebBaseLoader(
    url
)

docs = loader.load()

chain = prompt | model | parser

result = chain.invoke(
    {
        "question": "What is the exchange policy of this brand? give only in 3 lines.",
        "text": docs[0].page_content,
    }
)

print(result)
