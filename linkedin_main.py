from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from ThirdParty import linkedin as ln
from Agents import linkedin_url_lookup_agent as lu

"""
TODO:
1. Fetch Information of a Linkedin Profile and formatting it in JSON Format
2.Store The information in a JSON File
3. Use in LLM Model and generate Summary about the person
"""

if __name__ == "__main__":
    load_dotenv()
    url = lu.linkedin_url_lookup(name="Bill Gates")
    profile_information=ln.scrap_linkedin_profile(linkedin_url=url)

    file_path = "ThirdParty/data.json"
    with open(file_path, "r") as file:
        # Read the contents of the file
        content = file.read()
        # Print the contents
        # print(content)

    summary_template = """
    Given LinkedIn Information {information} about a Person from which I want you to create
    1. a short summary
    2. two interesting facts about them"""

    prompt = PromptTemplate(input_variables=["information"], template=summary_template)
    chatModel = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    chain = LLMChain(llm=chatModel, prompt=prompt)
    result = chain.invoke(input={"information": content})
    print(result["text"])
