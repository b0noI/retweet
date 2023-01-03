import os
import openai

from . import const 
from . import utils

from string import Template

SHAKESPEARE_TEMPLATE_STRING="""Rephrase following twitt in the way how Shakespeare could have phrase it. It still should be a twitter sized
----
$text"""
SHAKESPEARE_TEMPLATE = Template(SHAKESPEARE_TEMPLATE_STRING)

KANT_TEMPLATE_STRING="""Rephrase following tweet in the way how Immanuel Kant could have phrase it. It still should be a twitter sized
----
$text"""
KANT_TEMPLATE = Template(KANT_TEMPLATE_STRING)

MUSK_TEMPLATE_STRING="""Keeping the meaning re-write the following tweet in the way how Elon Musk could have twitted similar thought. Result still should be a twitter sized
----
$text"""
MUSK_TEMPLATE = Template(MUSK_TEMPLATE_STRING)

TRUMP_TEMPLATE_STRING="""Keeping the meaning re-write the following tweet in the way how Trump (the president) could have twitted similar thought. Result still should be a twitter sized
----
$text"""
TRUMP_TEMPLATE = Template(TRUMP_TEMPLATE_STRING)

JOKE_TEMPLATE_STRING="""Write message from the following tweet in a form of a joke (it is ok to be explicit and unpolite here). Result still should be a twitter sized
----
$text"""
JOKE_TEMPLATE = Template(JOKE_TEMPLATE_STRING)

def rephrase(text):
    prompt = KANT_TEMPLATE.substitute(text=text)
    openai.organization = const.GPT3_ORG_ID
    openai.api_key = utils.get_gpt3_secret()
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=280,
        temperature=0.9
    )
    return response["choices"][0]["text"].strip()


if __name__ == "__main__":
    print(
        rephrase(
            "BTW, if you are not happy about how little traffic google sends back to the sites from where it gets answers to the questions, just wait till ChatGPT like becomes popular."
            )
    )
