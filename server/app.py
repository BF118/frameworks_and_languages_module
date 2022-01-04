#https://medium.com/codex/buid-apis-with-falcon-in-python-all-essentials-you-need-9e2c2a5e1759
#https://careerkarma.com/blog/python-typeerror-list-indices-must-be-integers-or-slices-not-str/
#http GET localhost:8000/item/{id}/
#
#python3 -m http.server 8000
import falcon
import json
import datetime



from falcon.http_status import HTTPStatus
from wsgiref.simple_server import make_server
from datastore import *

class getResource():
    def on_get(self,req,resp ,itemId):
        
        setId = int(itemId) -1
        fetchedItem={}
        fetchedItem = datastore.get_item(setId)

        if not fetchedItem:
            resp.falcon.HTTP_404
        else:
            resp.status= falcon.HTTP_200
            resp.media ={"id" :fetchedItem.get('id') + 1}
        resp.content_type = "application/json"
    def on_delete(self, req, resp, itemId):

        item = {}
        item = datastore.get_item(itemId)
        setId = int(itemId) - 1

        item = datastore.get_item(fixedId)

        if not item:
            resp.status = falcon.HTTP_201
        else:
            datastore.delete_item(itemId)
            datastore.delete_item(setId)
            resp.status = falcon.HTTP_404


class getmultiResource():
   def on_get(self,req, resp):
        fetchedData = []

        resp.status = falcon.HTTP_200
        resp.content_type = "application/json"
        resp.media = fetchedData

class postResource():
    def on_post(self,req,resp):
        
        inputdata ={}
        inputdata = req.get_media()

        reqFields =set({'user_id', 'keywords', 'description', 'lat', 'lon'})
        givenFields = set(inputdata.keys())
        
        date_from = datetime.datetime.now().isoformat
        date_to = datetime.datetime.now().isoformat

        
        if(givenFields.issubset(reqFields)):
            inputdata['date_from'] = date_from
            inputdata['date_to'] = date_to
            newId = max(ITEMS.keys()) + 1
            datastore.create_item(inputdata)
            resp.media = {'id': newId}
            resp.content_type = "application/json"
            resp.status = falcon.HTTP_201
        else:
            resp.status = falcon.HTTP_405
        


def deleteResource():
    def on_delete(self,req, resp):
        resp.media = req.media
        resp.status = falcon.HTTP_404
        pass

class rootResource():
    def on_get(self,req ,resp):
        resp.body ="test"
        resp.content_type = "text/html"
        resp.status = falcon.HTTP_200

#https://github.com/falconry/falcon/issues/1220
class HandleCORS(object):
    def process_request(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods','POST')
        resp.set_header('Access-Control-Allow-Headers', 'Content-Type')
        resp.set_header('Access-Control-Max-Age', 1728000)  # 20 days
        if req.method == 'OPTIONS':
            raise HTTPStatus(falcon.HTTP_204, body='\n')



api = falcon.App(middleware=[HandleCORS() ])
api.add_route('/', rootResource())
api.add_route('/item', postResource())
api.add_route('/item/{userId}/',getResource())
api.add_route('/item/{userId}/',deleteResource())
api.add_route('/items', getmultiResource())
# change to spec routing

if __name__ == '__main__':
    with make_server('', 8000, api) as httpd:
        print('Serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()