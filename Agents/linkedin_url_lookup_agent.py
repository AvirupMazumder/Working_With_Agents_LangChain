from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI

from Tools.google_search_url import get_profile_url


def linkedin_url_lookup(name:str) -> str:
    load_dotenv()
    summary_template = """Given the full name of a person {name_of_person},
    I want you to get it to me the the linkedIn profile of the person.
    The answer should only contain the URL."""

    prompt = PromptTemplate(input_variables=["name_of_person"], template=summary_template)
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    tools_for_agent=[
        Tool(name="Using Google Search for Linkedin Profile Page",
             func=get_profile_url,
             description="Useful for when you need to get the Linkedin Page URL")
    ]
    agent = initialize_agent(tools=tools_for_agent, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    result = agent.invoke(input={"input": prompt.format_prompt(name_of_person=name)})
    return result["output"]



