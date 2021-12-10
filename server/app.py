#python3 -m http.server 8000
import falcon
import json
from wsgiref.simple_server import make_server



api = falcon.App()
class HTTPRequests():
    
    def on_get_single(self,req,resp):
        
        if req.param("id"):
            resp.media = {'id' : "", 'lat' : "", 'lon' : "", 'description' : "", 'keywords' : ""}
        
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON
        pass
    
    def on_get_multiple(self,req, resp):
        if req.param("id"):
            resp.media

            resp.status= falcon.HTTP_200
            resp.content_type = falcon.MEDIA_JSON
            pass

    def on_post(self,req,resp):
        
        resp.media = {'id' : itemId, 'lat' : lat, 'lon' : lon, 'description' : description, 'keywords' : keywords}
      
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON
        pass

    def on_del(self,req,resp):
        
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON
        pass




api.add_route('/item', HTTPRequests.on_post)
api.add_route('/item/{itemId}',HTTPRequests.on_get_single)
api.add_route('/items', HTTPRequests.on_get_multiple)
api.add_route('/item/{itemId}',HTTPRequests.on_del)
# change to spec routing

if __name__ == '__main__':
    with make_server('', 8000, api) as httpd:
        print('Serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()


#remove classes for each one