import socket
import json
import sys
import psutil
import time

HOST = 'localhost'
PORT = 5000
while True:
  
  
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect((HOST, PORT))  

  msg = {'Datos': str(psutil.cpu_percent())+"%"} 
  sock.send(str(json.dumps(msg) ).encode('utf-8') )
  time.sleep(35)

  sock.close()
sys.exit(0)
