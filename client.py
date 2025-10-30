import socket
from crypto_utils import encrypt_message, decrypt_message

key = "thisisasecretkey"  

client = socket.socket()
client.connect(("localhost", 12345))

while True:
    msg = input("You: ")
    enc_msg = encrypt_message(key, msg)
    client.send(enc_msg.encode())

    data = client.recv(1024).decode()
    print("Friend:", decrypt_message(key, data))
