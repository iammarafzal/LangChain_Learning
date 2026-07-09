from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()

def word_counter(text):
    return f"Total Joke's Words: {len(text.split())}"

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

prompt = PromptTemplate(
    template="Write a joke on {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

joke_generator = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'wordcounter': RunnableLambda(word_counter)
})

final_chain = RunnableSequence(joke_generator, parallel_chain)

result = final_chain.invoke({'topic': 'Media'})

print(result)