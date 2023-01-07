from string import Template
import firebase_admin
from firebase_admin import firestore

db = firestore.Client(project="social-investments-337201")

template_document = db.collection("retweet").document("templates")

def get_template(template_name):
    doc_data = template_document.get().to_dict()    
    return Template(doc_data[template_name])


def get_default_template_name():
    doc_data = template_document.get().to_dict()    
    return doc_data["DEFAULT"]


def get_templates_names():
    doc_data = template_document.get().to_dict()
    return list(doc_data.keys())
