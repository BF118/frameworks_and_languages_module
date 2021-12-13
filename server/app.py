#https://medium.com/codex/build-apis-with-falcon-in-python-all-essentials-you-need-9e2c2a5e1759
#http GET localhost:8000/item/{id}/
#
#python3 -m http.server 8000
import falcon
import json
from wsgiref.simple_server import make_server
from datastore import *

class getResource():
    def on_get(self,req,resp ,userId,):
        if req.params(id):
            resp.media = json.dumps(example)
        
            resp.status = falcon.HTTP_OK
            resp.content_type = falcon.MEDIA_JSON


class getmultiResource():
   def on_get(self,req, resp):
        #if req.get_param("id"):
            resp.media = example
            
            resp.status= falcon.HTTP_200
            resp.content_type = falcon.MEDIA_JSON
            pass

class postResource():
    def on_post(self,req,resp):
        app = json.load(req.bounded_stream)
        example.append(app)
        resp.text= "example added"
        resp.status = falcon.HTTP_201
        resp.content_type = falcon.MEDIA_JSON
    
class deleResource():
    def on_del(self,req,resp):
        
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON
        pass



api = falcon.App()

api.add_route('/item', postResource())
api.add_route('/item/{userId}/',getResource())
api.add_route('/items', getmultiResource())
api.add_route('/item/delete',deleResource())
# change to spec routing

if __name__ == '__main__':
    with make_server('', 8000, api) as httpd:
        print('Serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()


