import falcon
import json
get = [

]
post = [

]
delete = [

]
class getResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.text =json.dumps(get)
        resp.content_type = falcon.MEDIA_JSON
class postResource:
    def on_post(self,req,resp):
        resp.text =json.dumps(post)
        request = json.loads(req.stream.read())
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_JSON
class deleResource:
    def on_del(self,req,resp):
        resp.text= json.dumps(delete)
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_JSON

