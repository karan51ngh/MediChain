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
    global fn, ln, age, x
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

            (x[0]).send(VERIFICATION_POS.encode(FORMAT))
            block_data['fn'] = fn
            block_data['ln'] = ln
            block_data['age'] = age
            conn_data[x[0]] = block_data

        if msg == DISCONNECT_MESSAGE:
            DISCONNECT_MESSAGE_REPLY(conn, addr)
            connected = False

        if msg == PUSH_CHANGE_TO_BLOCKCHAIN:

            print(f"{addr}: Pushing change to Blockchain")
            print(
                f"data about to add: {conn_data[conn]['fn']}, {conn_data[conn]['ln']}...")
            print(x[1])
            conn.send(BLOCKCHAIN_PUSH.encode(FORMAT))
            print("sending fn")
            conn.send(conn_data[conn]['fn'].encode(FORMAT))
            print("sending ln")
            conn.send(conn_data[conn]['ln'].encode(FORMAT))
            print("sending age")
            conn.send(conn_data[conn]['age'].encode(FORMAT))
            print("data sent for addition")

        if msg == DONT_PUSH_CHANGE_TO_BLOCKCHAIN:
            print(
                f"{addr}: CANNOT PUSH CHANGES TO BLOCKCHAIN since the documents are not in order.\n Dequing the Request")
            del conn_data[conn]
            print("REMOVED")

    conn.close()


Hospitals_Sockets = []  # to store all the connections in the array


# dictionary to store block details, copy of it used to send to conn_data
block_data = dict()

conn_data = dict()  # GLobal dictionary to store all the blocks that need to be varified, key == the client hospital used for verification

fn = ''
ln = ''
age = ''
x = 0


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
