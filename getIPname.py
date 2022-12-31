import socket
#add url
hostname = 'google.com'
addr = socket.gethostbyname(hostname)
print('The address of', hostname, 'is', addr)
