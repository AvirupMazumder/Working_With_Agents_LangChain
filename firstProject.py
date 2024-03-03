from dotenv import load_dotenv

# import os

from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

"""
#TODO
Working with LangChain:
    1. PromptTemplate
    2. ChatOpenAI
    3. LLMChain
"""

if __name__ == "__main__":
    print("Hello Langchain!")
    load_dotenv()
    """print(os.getenv('OPENAI_API_KEY'))"""

    # information1 = """
    # SVM
    # """
    # information2 = """
    # CNN
    # """
    # summary_template = """
    # Difference between {information1} and {information2} in not more than 600 words
    # """
    information = "Bey blade"
    summary_template = "Tell me something about the series {information} "

    prompt = PromptTemplate(input_variables=["information"], template=summary_template)
    chatModel = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=chatModel, prompt=prompt)
    result = chain.invoke(input={"information": information})
    print(result)
