from wsgiref.simple_server import make_server
from . import rephrase

import falcon


class RephraseResource:
    
    def on_post(self, req, resp):
        """Handles GET requests"""
        req_obj = req.get_media()
        original_text = req_obj["text"]
        if not original_text:
            resp.status = falcon.HTTP_403
            return

        updated_text = rephrase.rephrase(original_text)
        resp.status = falcon.HTTP_200  # This is the default status
        resp.media = {"text": updated_text}

app = falcon.App()

# Resources are represented by long-lived class instances
rephrase_resrouce = RephraseResource()

# things will handle all requests to the '/' URL path
app.add_route('/rephrase', rephrase_resrouce)

if __name__ == '__main__':
    with make_server('', 8080, app) as httpd:
        print('Serving on port 8080...')

        # Serve until process is killed
        httpd.serve_forever()
