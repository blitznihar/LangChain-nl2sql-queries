from langchain_openai import ChatOpenAI
from langchain.prompts import(
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)

from langchain.agents import OpenAIFunctionsAgent, AgentExecutor

from dotenv import load_dotenv

from tools.sql import run_query_tool

load_dotenv()

chat = ChatOpenAI()

prompt = ChatPromptTemplate(
    messages=[
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
        
    ]
)

tools = [run_query_tool]

agent = OpenAIFunctionsAgent(
    llm=chat,
    prompt=prompt,
    tools=tools
)
agent_executor = AgentExecutor(
    agent=agent,
    verbose=False,
    tools=tools
)
def answerquestion(question):
    answer = agent_executor(question)
    return answer

answerquestion("How many products are in the database?")
# agent_executor("How many products are in the database?")

