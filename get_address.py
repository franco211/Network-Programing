import ipaddress

getIP = '0.0.0.0'
hostname = ipaddress.IPv4Network(getIP)
print(hostname)