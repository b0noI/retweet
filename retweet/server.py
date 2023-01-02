from wsgiref.simple_server import make_server

import falcon


class RetweetResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = falcon.MEDIA_TEXT  # Default is JSON, so override
        resp.text = ('\nTwo things awe me most, the starry sky '
                     'above me and the moral law within me.\n'
                     '\n'
                     '    ~ Immanuel Kant\n\n')

app = falcon.App()

# Resources are represented by long-lived class instances
retweet = RetweetResource()

# things will handle all requests to the '/' URL path
app.add_route('/', retweet)

if __name__ == '__main__':
    with make_server('', 8080, app) as httpd:
        print('Serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()
