from Crypto.Cipher import AES
import base64
import os

def pad(text):
    return text + (16 - len(text) % 16) * chr(16 - len(text) % 16)

def unpad(text):
    return text[:-ord(text[-1])]

def encrypt_message(key, raw):
    raw = pad(raw)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    encrypted = cipher.encrypt(raw.encode('utf-8'))
    return base64.b64encode(encrypted).decode('utf-8')

def decrypt_message(key, enc):
    enc = base64.b64decode(enc)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    decrypted = cipher.decrypt(enc).decode('utf-8')
    return unpad(decrypted)
