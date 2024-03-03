import os
import requests
from dotenv import load_dotenv
import json


"""
#TODO
scrap_linkedin_profile:
 1. extract information of persons linkedin profile and store in JSON File
 2. Remove empty information's and unnecessary information's like certifications, people also viewed.
"""


def scrap_linkedin_profile(linkedin_url):
    load_dotenv()
    final_answer = {}
    headers = {"Authorization": "Bearer " + os.getenv("BEARER_API_KEY")}
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    response = requests.get(api_endpoint, params={"url": linkedin_url}, headers=headers)
    result = response.json()

    for key, value in result.items():
        if value not in (None, [], "") and key not in (
            "people_also_viewed",
            "certifications",
        ):
            final_answer[key] = value

    with open("./ThirdParty/data.json", "w") as file:
        # Write data to the JSON file
        json.dump(final_answer, file)

    return final_answer
