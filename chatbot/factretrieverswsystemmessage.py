from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage
from langchain.prompts import(
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)

from langchain.agents import AgentExecutor, create_openai_functions_agent

from dotenv import load_dotenv

from tools.sql import run_query_tool, list_tables, describe_tables_tool

load_dotenv()

chat = ChatOpenAI()

tables = list_tables()
print(tables)


prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(content=(
            f"You are an AI that has access to a SQLite database.\n"
            f"The database has tables of: {tables}\n"
            "Do not make any assumptions about what tables exist "
            "or what columns exist. Instead, use the 'describe_tables' function"
        )),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
        
    ]
)

tools = [run_query_tool, describe_tables_tool]

agent = create_openai_functions_agent(
    llm=chat,
    prompt=prompt,
    tools=tools
)
agent_executor = AgentExecutor(
    agent=agent,
    verbose=True,
    tools=tools
)
def answerquestion(question):
    answer = agent_executor.invoke({"input": question})
    #"how many users who have provided their shipping addresses?
    return answer

