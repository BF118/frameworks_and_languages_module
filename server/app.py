#python3 -m http.server 8000
import falcon
import json
from views import getResource, postResource, deleResource


api = falcon.App()
api.add_route('/get', getResource())
api.add_route('/post', postResource())
api.add_route('/delete', deleResource())
# change to spec routing




if __name__ == '__main__':
    from wsgiref import simple_server
    httpd = simple_server.make_server(['0.0.0.0'], [8000],(api))
    try:
        log.info('start')
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass