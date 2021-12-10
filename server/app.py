#python3 -m http.server 8000
import falcon
import json
from wsgiref.simple_server import make_server



api = falcon.App()
class getResource():
    def on_get_single(self,req,resp):
        
        if req.param("id"):
            resp.media = {'id' : "", 'lat' : "", 'lon' : "", 'description' : "", 'keywords' : ""}
        
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON
        pass
class getmultiResource():
    def on_get_multiple(self,req, resp):
        if req.param("id"):
            resp.media

            resp.status= falcon.HTTP_200
            resp.content_type = falcon.MEDIA_JSON
            pass
class postResource():
    def on_post(self,req,resp):
        
        resp.media = {'id' : itemId, 'lat' : lat, 'lon' : lon, 'description' : description, 'keywords' : keywords}
      
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON
        pass
class deleResource():
    def on_del(self,req,resp):
        
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON
        pass




api.add_route('/item', postResource())
api.add_route('/item/{itemId}/',getResource())
api.add_route('/items', getmultiResource())
api.add_route('/item/{itemId}/',deleResource())
# change to spec routing

if __name__ == '__main__':
    with make_server('', 8000, api) as httpd:
        print('Serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()


#remove classes for each one