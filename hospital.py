import socket
from constants import *
from wrapper_funcs import *

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    client.send(msg.encode(FORMAT))


def recieve():
    return client.recv(HEADER).decode(FORMAT)


while True:
    ch = PRINT_MENU()

    if ch == 1:
        send(RECORD_UPDATE_REQUEST)
        if recieve() == INITIATE_MESSAGE:
            SEND_PATIENT_DETAILS(client)

    if ch == 2:
        send(DISCONNECT_MESSAGE)
        print(recieve())
        exit()

    else:
        continue
