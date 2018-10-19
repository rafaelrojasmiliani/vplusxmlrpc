
# Client code

import xmlrpclib
#import socket

#socket.setdefaulttimeout(5)
server = xmlrpclib.Server('http://10.10.238.33:5000')
print(server.cdeletem("xmlrpc.test"))

print('testing error')
print(server.nonexistingmethod("xmlrpc.test"))
