import struct
import socket

# Create a raw socket
sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

# Set the IP header fields
source_ip = '127.0.0.1'
dest_ip = '127.0.0.1'

# Create the IP header
ihl = 5
version = 4
tos = 0
tot_len = 20 + 8 # 20 bytes for the IP header, 8 bytes for the ICMP header
id = 54321  # Id of this packet
frag_off = 0
ttl = 255
protocol = socket.IPPROTO_ICMP
check = 10  # IP header checksum
saddr = socket.inet_aton ( source_ip )
daddr = socket.inet_aton ( dest_ip )

ihl_version = (version << 4) + ihl

# the ! in the pack format string means network order
ip_header = struct.pack('!BBHHHBBH4s4s' , ihl_version, tos, tot_len, id, frag_off, ttl, protocol, check, saddr, daddr)

# Create the ICMP header
type = 8 # ICMP Echo request
code = 0
checksum = 10
identifier = 0
sequence = 0

# the ! in the pack format string means network order
icmp_header = struct.pack('!BBHHH' , type, code, checksum, identifier, sequence)

# Create the ICMP packet
packet = ip_header + icmp_header

# Send the packet over the network
sock.sendto(packet, (dest_ip, 1))

# Close the socket
sock.close()
