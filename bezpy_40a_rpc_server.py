# https://www.tutorialspoint.com/python_network_programming/python_rpc_json_server.htm
# jsonrpclib is not a built in library, requires pip install jsonrpclib
# WARNING: have not got working yet


from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

def findlen(*args):
    res = []
    for arg in args:
        try:
            lenval = len(arg)
        except TypeError:
            lenval = None
        res.append((lenval, arg))
    return res

if __name__ == '__main__':
    server = SimpleJSONRPCServer(('localhost', 1006))
    server.register_function(findlen)
    print("Start server")
    server.serve_forever()    
 

