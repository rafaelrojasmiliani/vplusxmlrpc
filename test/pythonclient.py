'''
  Calls a XMLRPC running on the V+ server.
  This ill cal the the cdeletem
'''
# Client code

import xmlrpclib
#import socket

#socket.setdefaulttimeout(5)


def main():
    server = xmlrpclib.Server('http://10.10.238.33:5000')
    print(server.cdeletem("xmlrpc.test"))

    print('testing error')
    print(server.nonexistingmethod("xmlrpc.test"))
  
if __name__ == '__main__':
    main()
