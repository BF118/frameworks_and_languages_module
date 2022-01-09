#https://medium.com/codex/buid-apis-with-falcon-in-python-all-essentials-you-need-9e2c2a5e1759
#https://careerkarma.com/blog/python-typeerror-list-indices-must-be-integers-or-slices-not-str/
#https://httpstatusdogs.com/


import falcon
import json
import datetime


#Imports the HTTP statuses we need for our restapi
from falcon.http_status import HTTPStatus

#Imports a simple server so that the code can run locally and not having to build each time
from wsgiref.simple_server import make_server

#Imports everything from the datastore
from datastore import *

#set the base root for web server will shows test when loaded
class rootResource():
    def on_get(self,req ,resp):
        resp.body ="test"
        resp.content_type = "text/html"
        resp.status = falcon.HTTP_200

class getResource():
    def on_get(self,req,resp,itemId):#Request for a singular item

        #changes the itemId variable to setid 
        setId = req.get_params(itemId)
        #creates an empty dictionary that we then put the data in from the datestore
        fetchedItem={{}}
        fetchedItem = datastore.get_item(setId)

        #if the item isn't in fetched items sends a 404 error which is not found
        if not fetchedItem:
            resp.falcon.HTTP_404
        
        #responds to the get requests and shows the data for the specified id 
        else:
            resp.status= falcon.HTTP_200
            resp.media ={"id" :fetchedItem.get('id')}
        resp.content_type = "application/json"
    
    def on_delete(self, req, resp, itemId):
        #similar to get request set a variable for the id
        setId = int(itemId)

        #put the items from the datastore into a variable that we can use
        item = datastore.get_item(setId)

        if not item:
            resp.status = falcon.HTTP_404
        else:
            #if an item is in the datastore with the id we need it will be deleted
            datastore.delete_item(setId)
            resp.status = falcon.HTTP_201#spec wants a 201 request rather than 200
        resp.content_type = "application/json"


class getmultiResource():
   def on_get(self,req, resp):#request for all the data in the datastore
        fetchedData = []

        resp.status = falcon.HTTP_200
        resp.content_type = "application/json"
        resp.media = fetchedData


class postResource():
    def on_post(self,req,resp):#post requests for the server
        
        inputdata ={}
        inputdata = req.get_media()

        #creates 2 sets to compare to each other to make sure the right data has been input
        reqFields =set({'user_id', 'keywords', 'description', 'lat', 'lon','image'})
        givenFields = set(inputdata.keys())
        
        #creates times automatically that the user can change
        date_from = datetime.datetime.now().isoformat
        date_to = datetime.datetime.now().isoformat

        #checks the two sets from above if they have the same keys creates a new item in the datastore
        if(givenFields.issubset(reqFields)):
            inputdata['date_from'] = date_from
            inputdata['date_to'] = date_to
            newId = max(ITEMS.keys()) + 1
            datastore.create_item(inputdata)
            resp.media = {'id': newId}
            resp.content_type = "application/json"
            resp.status = falcon.HTTP_201
        
        #if sets aren't the same throws a 405 error for methods not allowed
        else:
            resp.status = falcon.HTTP_405
        


#https://github.com/falconry/falcon/issues/1220
class HandleCORS(object):
    def process_request(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods','POST, GET, DELETE')
        resp.set_header('Access-Control-Allow-Headers', 'Content-Type')
        resp.set_header('Access-Control-Max-Age', 1728000)
        if req.method == 'OPTIONS':
            raise HTTPStatus(falcon.HTTP_204, body='\n')


#applies the middleware above to the falcon app
api = falcon.App(middleware=[HandleCORS() ])

#routes for the post, get, delete requests
api.add_route('/', rootResource())
api.add_route('/item', postResource())
api.add_route('/item/{itemId}/',getResource())
api.add_route('/items', getmultiResource())

#allows the server to be run locally
if __name__ == '__main__':
    with make_server('', 8000, api) as httpd:
        print('Serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()