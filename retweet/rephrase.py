import os
import openai

from . import const 
from . import utils
from . import templates


def rephrase(text, template_name=templates.get_default_template_name()):
    template = templates.get_template(template_name)
    prompt = template.substitute(text=text)
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
            "BTW, if you are not happy about how little traffic google sends back to the sites from where it gets answers to the questions, just wait till ChatGPT like becomes popular.", "YODA"
            )
    )
