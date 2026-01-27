from langchain_core.prompts import PromptTemplate
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
# from tavily import TavilyClient
from langchain_tavily import TavilySearch

load_dotenv()

# tavily = TavilyClient()

# @tool
# def search(query: str) -> str:
#     """
#     Tool for searching weather

#     Args:
#         query: The query to search for
    
#     Returns:
#         The search result
#     """
#     print(f"Searching for {query}")
#     return tavily.search(query=query)

llm = ChatOllama(model="gpt-oss:20b")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)


def main():
    result = agent.invoke({"messages":HumanMessage(content="Search about 5 job postings in AI domain by Syngenta in India. Use only linkedin for searching")})
    print(result)


if __name__ == "__main__":
    main()
