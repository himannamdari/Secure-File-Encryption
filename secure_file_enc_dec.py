import os
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def generate_key(passphrase):
    """Generates a 32-byte AES key from a passphrase."""
    return hashlib.sha256(passphrase.encode()).digest()

def encrypt_file(input_file, output_file, passphrase):
    """Encrypts a file using AES-256 and Base64 encoding."""
    key = generate_key(passphrase)
    iv = os.urandom(16)  # Generate a random IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    encrypted_data = base64.b64encode(iv + ciphertext).decode()
    
    with open(output_file, 'w') as f:
        f.write(encrypted_data)
    
    print(f"File '{input_file}' encrypted successfully as '{output_file}'.")

def decrypt_file(input_file, output_file, passphrase):
    """Decrypts a Base64-encoded AES-256 encrypted file."""
    key = generate_key(passphrase)
    
    with open(input_file, 'r') as f:
        encrypted_data = base64.b64decode(f.read())
    
    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    
    with open(output_file, 'wb') as f:
        f.write(plaintext)
    
    print(f"File '{input_file}' decrypted successfully as '{output_file}'.")

if __name__ == "__main__":
    option = input("Do you want to (E)ncrypt or (D)ecrypt a file? ").strip().lower()
    
    if option == 'e':
        input_file = input("Enter the file to encrypt: ").strip()
        output_file = input("Enter the output encrypted file: ").strip()
        passphrase = input("Enter a secure passphrase: ").strip()
        encrypt_file(input_file, output_file, passphrase)
    elif option == 'd':
        input_file = input("Enter the encrypted file to decrypt: ").strip()
        output_file = input("Enter the output decrypted file: ").strip()
        passphrase = input("Enter the passphrase: ").strip()
        decrypt_file(input_file, output_file, passphrase)
    else:
        print("Invalid option. Please choose 'E' for encryption or 'D' for decryption.")
