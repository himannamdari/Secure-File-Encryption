#  Secure File Encryption & Decryption

## Overview
This project provides a simple **AES-256** encryption and decryption tool for text files. It allows users to securely encrypt files using a **passphrase** and later decrypt them back to their original form. The tool also applies **Base64 encoding** to store encrypted data safely.

##  Features
- **AES-256 Encryption** – Industry-standard encryption.
- **Base64 Encoding** – Prevents data corruption.
- **Passphrase Security** – User-defined key for encryption/decryption.
- **Handles Any Text File** – Encrypt and decrypt sensitive data easily.

##  How It Works
###  Encryption Process
1. User provides a **text file** and a **passphrase**.
2. The file content is **encrypted using AES-256**.
3. The encrypted data is **Base64-encoded and saved**.

###  Decryption Process
1. User provides an **encrypted file** and the **correct passphrase**.
2. The **Base64 encoding is reversed**.
3. The data is **decrypted using AES-256** to restore the original file.

##  Usage
### Prerequisites
Ensure you have **Python 3** and install the required library:
```bash
pip install pycryptodome
```

### Running the Script
```bash
python secure_file_enc_dec.py
```

### Example
#### Encryption
```
Do you want to (E)ncrypt or (D)ecrypt a file? E
Enter the file to encrypt: secret.txt
Enter the output encrypted file: secret.enc
Enter a secure passphrase: mypassword
File 'secret.txt' encrypted successfully as 'secret.enc'.
```
#### Decryption
```
Do you want to (E)ncrypt or (D)ecrypt a file? D
Enter the encrypted file to decrypt: secret.enc
Enter the output decrypted file: decrypted.txt
Enter the passphrase: mypassword
File 'secret.enc' decrypted successfully as 'decrypted.txt'.
```

## Contributing
1. Fork the repo.
2. Create a new branch (`feature-branch`).
3. Make your improvements.
4. Submit a Pull Request.

##  License
This project is licensed under the **MIT License**. Feel free to use and modify it!
