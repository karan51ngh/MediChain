import socket
import threading
import random
from constants import *
from wrapper_funcs import *

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def chooseRandomNodeForVerification(hs, y):
    # Needs at least 2 hospitals in the network else exception
    while True:
        x = random.choice(hs)
        if x == y:
            pass
        else:
            return x


def recieve(conn):
    return conn.recv(HEADER).decode(FORMAT)


def handle_client(conn, addr):
    print(f"NEW CONNECTION: {addr} connected\n.")

    connected = True
    while connected:
        msg = recieve(conn)
        if msg == RECORD_UPDATE_REQUEST:
            ASK_PATIENT_DETAILS(conn, addr)
            fn, ln, age = RECIEVE_PATIENT_DETAILS(conn, addr)
            print(
                f"RECIEVED DETAILS: F.Name = {fn}, L.Name = {ln}, Age = {age},\nInitializing Verification.")

            # print(f"The available hopitals in the network are: {Hospitals_Sockets}")

            x = chooseRandomNodeForVerification(
                Hospitals_Sockets, (conn, addr))
            print(f"Hospital CHOSEN for VERIFICATION is {x[1]}\n")

        if msg == DISCONNECT_MESSAGE:
            DISCONNECT_MESSAGE_REPLY(conn, addr)
            connected = False

    conn.close()


Hospitals_Sockets = []  # to store all the connections in the array


def start():
    server.listen()
    print(f"Government Node Initiated on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(
            f"Number of Hospitals in the network is: {threading.active_count() - 1}\n")
        Hospitals_Sockets.append((conn, addr))


start()
