import subprocess as sp
import socket
import sys
from ipaddress import ip_address, IPv4Address

# def ip_look(ip):
#     look = sp.Popen(['nslookup',ip],stdout=sp.PIPE).communicate()[0]
#     look = look.decode('utf-8')
#     return(look)



# def ip_look(IP: str) -> str:
#     try:
#         ip = socket.gethostbyname(hostname)
#         return(f'The {hostname} IP Address is {ip}')
#     except socket.gaierror as e:
#         return(f'Invalid hostname, error raised is {e}')

# def ip_look(IP: str) -> str:
#     try:
#         return "IPv4" if type(ip_address(IP)) is IPv4Address else "IPv6"
#     except ValueError:
#         return "Invalid"



# def ip_look(ip):
#     ip_list = []
#     if '\n' in ip:
#         for ip in ip.split('\n'):
#             if '\r' in ip:
#                 ip=ip.strip('\r')
#             ip_list.append(ip_check(ip))
#         return(ip_list)
#     ip_list.append(ip_check(ip))
#     return(ip_list)
#
# def ip_check(ip):
#     ping_statistics = {}
#     ping = sp.Popen(['ping',ip],stdout=sp.PIPE).communicate()[0]
#     ping_statistics['ip'] = ip
#     #print(ping)
#     ping = ping.decode('utf-8')
#     #print(ping)
#     results = ping.split(f'Ping statistics for {ip}:')[1]
#     sent = results.split('Sent =')[1].split()[0].strip(",")
#     received = results.split('Received =')[1].split()[0].strip(",")
#     lost = results.split('Lost =')[1].split()[0].strip(",")
#     ping_statistics['sent'] = sent
#     ping_statistics['received'] = received
#     ping_statistics['lost'] = lost
#     print(sent,received,lost)
#     return(ping_statistics)
# #print(ip_check('192.168.0.1'))