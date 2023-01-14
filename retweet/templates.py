from string import Template
import firebase_admin
from firebase_admin import firestore

db = firestore.Client(project="social-investments-337201")

template_collection = db.collection("retweet-templates")

def get_template(template_name): 
    return Template(get_teamplate_raw_string(template_name))


def get_teamplate_raw_string(template_name):
    doc = template_collection.where("template_name", "==", template_name).limit(1).get()    
    return doc[0].get("template_value")


def get_default_template_name():
    doc = template_collection.where("template_name", "==", "DEFAULT").limit(1).get()    
    return doc[0].get("template_value")


def get_templates_names():
    docs = template_collection.where("template_name", ">", "").get()  
    return list(doc.get("template_name") for doc in docs)
