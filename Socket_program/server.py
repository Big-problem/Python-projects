import socket
import threading

PORT = 5050
# SERVER = "10.0.0.22" # The IPv4 address of this laptop 
SERVER = socket.gethostbyname(socket.gethostname()) # Get the address by code
ADDR = (SERVER, PORT)
HEADER = 64 # length of the message
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

# Make new socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn: socket.socket, addr):
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        # Receive the length of the message first
        # then receive the actual msg according to the length
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            
            conn.send("Message received".encode(FORMAT))

    conn.close()

def start():
    server.listen()
    print(f"[Listening] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept() # This line will keep running if nothing accept
                                     # So we need to use threaning to prevent blocking other request
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()}") # 一開始accept後到這行只有一個[start]的thread
                                     # 真正thread.start()後會有2個thread, 為了只顯示thread.start()的thread數, 就不另外減1了
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()



if __name__ == "__main__":
    print("[STARTING] server is starting...")
    start()