from constants import *
import socket
from wrapper_funcs import *
from blockchain import *
from helperFunctions import *
import datetime


def PRINT_MENU():
    print("What do You want to do?")
    print("1: Update A Patient Record")
    print("2: Disconnect from the Network")
    print("3: IDLE\n")
    ch = int(input())
    return ch


def DISCONNECT_MESSAGE_REPLY(conn, addr):
    print(f"{addr} Has Been Disconnected")
    conn.send(
        f"You are DISCONNECTED from the NETWORK\n".encode(FORMAT))


def ASK_PATIENT_DETAILS(conn, addr):
    print(f"{addr} wants to add a Patient Record\n")
    conn.send(INITIATE_MESSAGE.encode(FORMAT))


def RECIEVE_PATIENT_DETAILS(conn, addr):
    print(f"Waiting for the Patient Details\n")
    fn = conn.recv(HEADER).decode(FORMAT)
    ln = conn.recv(HEADER).decode(FORMAT)
    age = conn.recv(HEADER).decode(FORMAT)
    return [fn, ln, age]


def SEND_PATIENT_DETAILS(client):
    print("Requesting Patient Documents")
    fn = input("Enter the First Name of the Patient: ")
    client.send(fn.encode(FORMAT))
    ln = input("Enter the Last Name of the Patient: ")
    client.send(ln.encode(FORMAT))
    age = input("Enter the Age of the Patient: ")
    client.send(age.encode(FORMAT))


def blockchain_update_final_push(fn, ln, age):
    bc = Blockchain()
    prev_block = bc.get_last_block()
    idx = str(len(bc.chain) + 1)
    # fn = "Carl"
    # ln = "Jung"
    # age = "85"
    dt = str(datetime.datetime.now())
    phv = str(bc.hash(prev_block))
    new_proof, hash_val = bc.mining(idx, fn, ln, age, dt, phv)

    print(
        f'the new nonce is {new_proof} and the hash value of our block is {hash_val}')
    update_patient_record(idx, fn, ln, age, dt, phv, new_proof)
