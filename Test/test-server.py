# coding: utf-8

__author__ = 'Yemilice_lau'


from xmlrpc.server import SimpleXMLRPCServer

class SimpleRpcServer:
    _rpc_methods_ = ['PrintWork']
    def __init__(self, address):
        self._serv = SimpleXMLRPCServer(address, allow_none=True)
        for name in self._rpc_methods_:
            self._serv.register_function(getattr(self, name))

    def PrintWork(self, name):
        print(name)

    def serve_forever(self):
        self._serv.serve_forever()

# Example
if __name__ == '__main__':
    print("服务开始.....")
    kvserv = SimpleRpcServer(('127.0.0.1', 7900))
    kvserv.serve_forever()