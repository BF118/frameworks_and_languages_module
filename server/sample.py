# sample.py

import falcon

class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }

        resp.media = quote

app = falcon.App()
app.add_route('/quote', QuoteResource())

if __name__ == '__main__':


    from wsgiref import simple_server
    httpd = simple_server.make_server(['0.0.0.0'], ['8000'],create_wsgi_app (app))
    try:
        log.info('start')
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass