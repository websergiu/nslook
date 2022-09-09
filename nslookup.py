import subprocess as sp
import socket
import sys

def ip_look(ip):
    look = sp.Popen(['nslookup',ip],stdout=sp.PIPE).communicate()[0]
    look = look.decode('utf-8')
    return(look)