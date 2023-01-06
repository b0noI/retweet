from wsgiref.simple_server import make_server

from . import rephrase, templates
import firebase_admin
from firebase_admin import firestore

import falcon

firebase_admin.initialize_app()

db = firestore.Client(project="social-investments-337201")

class RephraseResource:

    def on_post(self, req, resp):
        """Handles POST requests"""
        req_obj = req.get_media()
        original_text = req_obj["text"]
        template_name = templates.get_default_template_name()
        if "template_name" in req_obj:
            template_name = req_obj["template_name"]
        if not original_text:
            resp.status = falcon.HTTP_403
            return

        updated_text = rephrase.rephrase(original_text, template_name=template_name)
        db.collection("retweet").add({
            "timestamp": firestore.SERVER_TIMESTAMP,
            "text": original_text,
            "rephrased_text": updated_text
        })
        resp.status = falcon.HTTP_200
        resp.media = {"text": updated_text}


class TemplatesResource:

    def on_get(self, req, resp):
        """Handles GET requests"""

        resp.status = falcon.HTTP_200
        resp.media = templates.get_templates_names()


app = falcon.App(cors_enable=True)

rephrase_resrouce = RephraseResource()
templates_resrouce = TemplatesResource()

app.add_route('/rephrase', rephrase_resrouce)
app.add_route('/templates', templates_resrouce)

if __name__ == '__main__':
    with make_server('', 8080, app) as httpd:
        print('Serving on port 8080...')

        # Serve until process is killed
        httpd.serve_forever()
