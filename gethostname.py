import socket

getIP = '0.0.0.0'
hostname = socket.getfqdn(getIP)

if hostname is None:
    print(f'Unable to resolve FQDN for IP address {getIP}')
else:
    print(f'The FQDN for {getIP} is {hostname}')