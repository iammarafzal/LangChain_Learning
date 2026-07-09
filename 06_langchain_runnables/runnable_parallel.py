from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Write a post on {topic}',
    input_variables=['topic']
)

parallel_runnable = RunnableParallel(
    {
        'tweeter': RunnableSequence(prompt, model, parser),
        'linkedin': RunnableSequence(prompt, model, parser)
    }
)

result = parallel_runnable.invoke({'topic': 'Innovations after revolution of AI'})

print("Tweet:\n", result['tweeter'])
print("-" * 10)
print("Linkedin:\n", result['linkedin'])