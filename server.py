import socket
from crypto_utils import encrypt_message, decrypt_message

key = "thisisasecretkey"

server = socket.socket()
server.bind(("localhost", 12345))
server.listen(1)
print("Server running... Waiting for connection...")

conn, addr = server.accept()
print("Connected to:", addr)

while True:
    data = conn.recv(1024).decode()
    print("Friend:", decrypt_message(key, data))

    msg = input("You: ")
    enc_msg = encrypt_message(key, msg)
    conn.send(enc_msg.encode())
