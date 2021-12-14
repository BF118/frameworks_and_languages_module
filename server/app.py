#https://medium.com/codex/buid-apis-with-falcon-in-python-all-essentials-you-need-9e2c2a5e1759
#https://careerkarma.com/blog/python-typeerror-list-indices-must-be-integers-or-slices-not-str/
#http GET localhost:8000/item/{id}/
#
#python3 -m http.server 8000
import falcon
import json
import datetime
from wsgiref.simple_server import make_server
from datastore import *

class getResource():
    def on_get(self,req,resp ,userId,):
        #if req.params(example["id"]):
            resp.media = json.dumps(ITEMS)
        
            resp.status = falcon.HTTP_OK
            resp.content_type = falcon.MEDIA_JSON
    
    def on_delete(self,req,resp, userId):
        
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON
        pass

class getmultiResource():
   def on_get(self,req, resp):
        #if req.get_param("id"):
            resp.media = ITEMS
            
            resp.status= falcon.HTTP_200
            resp.content_type = falcon.MEDIA_JSON
            pass

class postResource():
    def on_post(self,req,resp):
        app = json.load(req.bounded_stream)
        
        date_from = datetime.datetime.now()
        date_to = datetime.datetime.now()
        
        fields =set({'user_id', 'keywords', 'description', 'lat', 'lon', 'date_from', 'date_to'})
        if ITEMS.keys() != fields:
            resp.status = falcon.HTTP_204
        else:
            app.update(ITEMS)
            resp.text= "Data added"
            resp.status = falcon.HTTP_201
    #_id = max(ITEMS.keys()) + 1
        
        resp.content_type = falcon.MEDIA_JSON


api = falcon.App(middleware=falcon.CORSMiddleware(
    allow_origins='http//:localhost:8001', allow_credentials='*'))

class rootResource():
    def on_get(self,req ,resp):
        
        resp.status = falcon.HTTP_200



api.add_route('/', rootResource())
api.add_route('/item', postResource())
api.add_route('/item/{userId}/',getResource())
api.add_route('/items', getmultiResource())
# change to spec routing

if __name__ == '__main__':
    with make_server('', 8000, api) as httpd:
        print('Serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()