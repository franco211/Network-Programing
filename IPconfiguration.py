import ipaddress

# Define the IPv4 address and network mask
ipv4_address = '192.0.2.1'
ipv4_mask = '255.255.255.0'

# Create an IPv4 interface object
ipv4_interface = ipaddress.ip_interface(f'{ipv4_address}/{ipv4_mask}')

# Print the interface details
print(f'IPv4 interface: {ipv4_interface.with_prefixlen}')
print(f'IPv4 address: {ipv4_interface.ip}')
print(f'IPv4 network: {ipv4_interface.network}')
print(f'IPv4 hostmask: {ipv4_interface.hostmask}')

# Define the IPv6 address and prefix length
ipv6_address = '2001:db8::1'
ipv6_prefix = 64

# Create an IPv6 interface object
ipv6_interface = ipaddress.ip_interface(f'{ipv6_address}/{ipv6_prefix}')

# Print the interface details
print(f'IPv6 interface: {ipv6_interface.with_prefixlen}')
print(f'IPv6 address: {ipv6_interface.ip}')
print(f'IPv6 network: {ipv6_interface.network}')
print(f'IPv6 hostmask: {ipv6_interface.hostmask}')
