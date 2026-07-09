from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

prompt1 = PromptTemplate(
    template="Write a joke on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Write a brief explanation on this {joke}",
    input_variables=['joke']
)

parser = StrOutputParser()

joke_generator = RunnableSequence(prompt1, model, parser)

parallel_runnable = RunnableParallel({
    'joke': RunnablePassthrough(),
    'joke_explainer': RunnableSequence(prompt2, model, parser)
})

final_runnable = RunnableSequence(joke_generator, parallel_runnable)

result = final_runnable.invoke({'topic': 'Media'})

print(result)