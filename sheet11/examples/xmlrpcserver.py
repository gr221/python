
import xmlrpc.server as xs
import socketserver
import time

## Wichtig!! Das MixIn muss VOR der eigentlichen Klasse kommen
class MyServer(socketserver.ForkingMixIn, xs.SimpleXMLRPCServer):
#class MyServer(xs.SimpleXMLRPCServer):
    def _dispatch(self, method, params):
        try:
            func = getattr(self, 'export_' + method)
        except:
            raise Exception("no func")
        else:
            return func(*params)

    def export_add(self, x, y):
        time.sleep(5)
        return x + y
    def export_arr(self, n):
        return [i*i for i in range(1, n + 1)]
    def export_com(self):
        return { 'nummer':7, \
                'liste': [1, "string", 8], \
                'hash': {\
                    'sub': "sstring",
                    'ary': [1,3,5,7]}}

s = MyServer(("localhost",8001))
s.serve_forever()

