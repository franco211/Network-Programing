import socket
#add url
hostname = 'comcast.net'
#resolve hostname
addr = socket.gethostbyname(hostname)
print('The address of', hostname, 'is', addr)
