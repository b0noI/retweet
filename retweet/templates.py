from string import Template
import firebase_admin
from firebase_admin import firestore

db = firestore.Client(project="social-investments-337201")

template_document = db.collection("retweet").document("templates")

doc_data = template_document.get().to_dict()

def get_template(template_name):    
    return Template(doc_data[template_name] + "\n----\n$text")


def get_default_template_name():    
    return doc_data["DEFAULT"]


def get_templates_names():
    return list(doc_data.keys())
