from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnablePassthrough, RunnableBranch

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

prompt1 = PromptTemplate(
    template="Write a detailed explaination {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Summarize the give text \n {text}",
    input_variables=['text']
)

parser = StrOutputParser()

report_generator = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableBranch(
    (lambda x: len(x.split())>300, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_generator, parallel_chain)

result = final_chain.invoke({'topic': 'Russia Vs America in Economy'})

print(result)