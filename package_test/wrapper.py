import aes
from aes import aes_encrypt
import caeser
from caeser import caesar_encrypt
import os

def encrypt_file(file_path, method):
    with open(file_path, 'r') as file:
        data = file.read()

    if method == 'aes':
        encrypted_data = aes_encrypt(data)
    elif method == 'caesar':
        shift = int(input("Enter the shift value for Caesar cipher: "))
        encrypted_data = caesar_encrypt(data, shift)
    else:
        print("Invalid method")
        return

    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    output_file_path = os.path.join(output_dir, 'encrypted_' + os.path.basename(file_path))

    with open(output_file_path, 'wb') as file:
        file.write(encrypted_data)

    print(f"Encrypted file saved at {output_file_path}")

def main():
    file_path = input("Enter the path of the file to encrypt: ")
    method = input("Enter the encryption method (aes/caesar): ")
    encrypt_file(file_path, method)

if __name__ == "__main__":
    main()