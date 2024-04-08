import cryptography
from cryptography.fernet import Fernet

def aes_encrypt(data):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(data.encode('utf-8'))
    return cipher_text, key