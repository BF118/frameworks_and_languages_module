import falcon

class CatalogItem(object):
    def on_get(self, req, resp):
        route_path = str(req.path) 
        if route_path.startswith("/quote"):   
            quote = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }
        elif route_path.startswith("/test"):
            quote = {
            'quote': (
                "hello world"
            ),
            'test': 'test'
        }
        elif route_path.startswith("/quote2"):
            quote = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }
        
        
        
        
        
        
        resp.media = quote



api = falcon.App()
api.add_route('/quote2', CatalogItem())
api.add_route('/test', CatalogItem())
api.add_route('/quote', CatalogItem())