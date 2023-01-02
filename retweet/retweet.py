import os
import openai

from . import const 
from . import utils

from string import Template

SHAKESPEARE_TEMPLATE_STRING="""Rephrase following twitt in the way how Shakespeare could have phrase it. It still should be a twitter sized
----
$text"""
SHAKESPEARE_TEMPLATE = Template(SHAKESPEARE_TEMPLATE_STRING)

def rephrase(text):
    prompt = SHAKESPEARE_TEMPLATE.substitute(text=text)
    openai.organization = const.GPT3_ORG_ID
    openai.api_key = utils.get_gpt3_secret()
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=280,
        temperature=0.7
    )
    return response["choices"][0]["text"]


if __name__ == "__main__":
    print(
        rephrase(
            "In the new year I do promiss to write here more. My appologies I was away lately, but I was working on something VERY exiting"
            )
    )
