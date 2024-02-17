import socket

PORT = 5050
HEADER = 64 # length of the message
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "10.0.0.22"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg:str):
    message = msg.encode(FORMAT) # Encode the string into bytes
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

msg = input()
send(msg)
msg = input()
send(msg)
msg = input()
send(msg)
send(DISCONNECT_MESSAGE)