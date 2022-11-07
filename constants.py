HEADER = 4096
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
RECORD_UPDATE_REQUEST = "!UPDATE_RECORD"
THANK_YOU_MESSAGE = "!THANK_YOU!"
INITIATE_MESSAGE = "!REQUESTING_DOCS"


def PRINT_MENU():
    print("What do You want to do?")
    print("1: Update A Patient Record")
    print("2: Disconnect from the Network\n")
    ch = int(input())
    return ch


def DISCONNECT_MESSAGE_REPLY(conn, addr):
    print(f"[{addr}] Has Been Disconnected")
    conn.send(
        f"You are DISCONNECTED from the NETWORK\n".encode(FORMAT))


def ASK_PATIENT_DETAILS(conn, addr):
    print(f"[{addr}] wants to add a Patient Record\n")
    conn.send(INITIATE_MESSAGE.encode(FORMAT))


def RECIEVE_PATIENT_DETAILS(conn, addr):
    print(f"[{addr}] Sending Patient Details\n")
    fn = conn.recv(HEADER).decode(FORMAT)
    ln = conn.recv(HEADER).decode(FORMAT)
    age = conn.recv(HEADER).decode(FORMAT)
    return [fn, ln, age]


def SEND_PATIENT_DETAILS(client):
    print("Requesting Patient Documents")
    fn = input("Enter the First Name of the Patient:")
    client.send(fn.encode(FORMAT))
    ln = input("Enter the Last Name of the Patient:")
    client.send(ln.encode(FORMAT))
    age = input("Enter the Age of the Patient:")
    client.send(age.encode(FORMAT))
