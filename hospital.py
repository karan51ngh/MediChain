import socket
from constants import *
from wrapper_funcs import *

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

# initializing a hospital socket
hosptl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hosptl.connect(ADDR)  # connecting to the government node

# Send Message to the Government Node.


def send(msg):
    hosptl.send(msg.encode(FORMAT))

# Recieve Message from the Government Node.


def recieve():
    return hosptl.recv(HEADER).decode(FORMAT)


while True:
    ch = PRINT_MENU()

    if ch == 1:
        send(RECORD_UPDATE_REQUEST)
        if recieve() == INITIATE_MESSAGE:
            SEND_PATIENT_DETAILS(hosptl)

    if ch == 2:
        send(DISCONNECT_MESSAGE)
        print(recieve())
        exit()

    else:
        continue
