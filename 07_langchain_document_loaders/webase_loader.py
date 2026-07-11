import os
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
os.environ.setdefault(
    "USER_AGENT", "LangChainLearningBot/1.0 (educational web-loader test)"
)

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

url = "https://example.com"

loader = WebBaseLoader(
    url,
    header_template={
        "User-Agent": "LangChainLearningBot/1.0 (educational web-loader test)"
    },
)

docs = loader.load()

chain = prompt | model | parser

result = chain.invoke(
    {
        "question": "What is this example domain intended for?",
        "text": docs[0].page_content,
    }
)

print(result)
