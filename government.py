import socket
import threading
from constants import *

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def recieve(conn):
    return conn.recv(HEADER).decode(FORMAT)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg = recieve(conn)
        if msg == RECORD_UPDATE_REQUEST:
            ASK_PATIENT_DETAILS(conn, addr)
            fn, ln, age = RECIEVE_PATIENT_DETAILS(conn, addr)
            print(
                f"Recieved Details: F.Name = {fn}, L.Name = {ln}, Age = {age}")

        if msg == DISCONNECT_MESSAGE:
            DISCONNECT_MESSAGE_REPLY(conn, addr)
            connected = False

    conn.close()


def start():
    server.listen()
    print(f"Government Node Initiated on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(
            f"Number of Hospitals in the network is: {threading.active_count() - 1}")


start()
