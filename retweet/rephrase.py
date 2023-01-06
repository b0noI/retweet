import os
import openai
import firebase_admin
from firebase_admin import firestore

from . import const 
from . import utils
from . import templates

firebase_admin.initialize_app()

db = firestore.client()



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
    
    rephrased_text = response["choices"][0]["text"].strip()
    doc_ref = db.collection("retweet").add({
        'timestamp': firestore.SERVER_TIMESTAMP,
        "text": text,
        "rephrased_text": rephrased_text
    })
    return rephrased_text

if __name__ == "__main__":
    print(
        rephrase(
            "BTW, if you are not happy about how little traffic google sends back to the sites from where it gets answers to the questions, just wait till ChatGPT like becomes popular.", "YODA"
            )
    )
