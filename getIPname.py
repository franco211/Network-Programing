import socket
#add url
hostname = 'comcast.net'
#resolve hostname
addr = socket.gethostbyname(hostname)
if addr is None:
    print(f'Unable to get ip address for {hostname}')
else:
        print('The address of', hostname, 'is', addr)
