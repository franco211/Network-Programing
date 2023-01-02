import socket
dns = socket.getservbyname('domain')
name = socket.getaddrinfo('tcp', 'port')
print(dns)

print(name)