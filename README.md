# Secure File Encryption & Decryption Tool

## Overview

The Secure File Encryption & Decryption Tool is a Python-based cybersecurity utility designed to protect sensitive data through strong cryptographic techniques.

This project demonstrates practical implementation of:

* Password-based key derivation
* Symmetric encryption using modern cryptography
* File integrity verification
* Secure handling of user data

It simulates a real-world security utility that can be used to safeguard confidential files from unauthorized access.

The system combines encryption, hashing, and authentication concepts to create a complete secure file workflow.


## Key Features

* AES-based secure file encryption using Fernet
* Password-derived encryption keys (PBKDF2 + SHA-256)
* Automatic random salt generation
* File integrity verification using SHA-256 hashing
* Protection against wrong password attempts
* Detection of tampered or corrupted files
* Command-line interactive interface
* Cross-platform compatibility


## Cryptographic Concepts Implemented

This project demonstrates real cybersecurity engineering practices:

* Key derivation from passwords (PBKDF2HMAC)
* Secure random salt generation
* Symmetric encryption with authenticated encryption mode
* File hashing for integrity verification
* Secure storage structure for encrypted data

These mechanisms simulate how secure storage systems and encrypted file vaults operate in production environments.



## Project Structure
```
secure-file-encryption-tool/
│
├── secure_file_tool.py      # Main encryption & decryption logic
├── test.txt                 # Sample file for testing
├── README.md                # Project documentation
└── .vscode/                 # Editor configuration
```



## Technologies Used

* Python 3
* cryptography library
* hashlib
* os module
* base64 encoding
* secure random number generation


## How the Tool Works

### Encryption Flow

1. User selects encryption option
2. Password is entered securely
3. Random salt is generated
4. Key is derived using PBKDF2 + SHA-256
5. Original file hash is calculated
6. File content is encrypted
7. Encrypted file is saved with:
	* Salt
	* Original hash
	* Encrypted data

### Decryption Flow
1. User selects decryption option
2. Password is requested
3. Salt and stored hash are extracted
4. Key is regenerated using password + salt
5. File is decrypted
6. Integrity hash is recalculated
7. Tool verifies if file was modified or corrupted


## Usage

### Run the program
```
python secure_file_tool.py
```

### Terminal Example — Encryption

```
Secure File Encryption Tool
1. Encrypt File
2. Decrypt File
Choose option (1/2): 1
Enter file name to encrypt: test.txt
Enter password: ********

File encrypted successfully.
Encrypted file: test.txt.enc
Integrity hash stored securely.
```

### Terminal Example — Decryption

```
Secure File Encryption Tool
1. Encrypt File
2. Decrypt File
Choose option (1/2): 2
Enter file name to decrypt: test.txt.enc
Enter password: ********

File decrypted successfully.
Integrity Verified: File is authentic.
Decrypted file: test.txt_decrypted
```

### Wrong Password Example
```
Wrong password or corrupted file.
```

### Tampered File Example

```
Warning: Integrity compromised!
```


## Security Strength

This project demonstrates strong defensive cybersecurity engineering skills:

* Prevents unauthorized file access
* Detects data tampering attempts
* Implements industry-grade cryptographic practices
* Protects confidentiality and integrity simultaneously
* Demonstrates secure software development mindset


## Performance

* Processes files efficiently using chunk-based hashing
* Lightweight encryption suitable for local systems
* Fast password-based key derivation
* Minimal memory footprint


## Security & Ethical Use

This project is intended for:

* Cybersecurity education
* Secure programming practice
* Cryptography learning
* Defensive security research

It should not be used for malicious concealment of illegal data.


## Learning Objectives

Through this project, the following cybersecurity skills are demonstrated:

* Applied cryptography implementation
* Secure key management concepts
* File integrity validation mechanisms
* Defensive secure software engineering
* Password-based encryption design
* Practical security tool development


## Author

Developed as part of a hands-on cybersecurity learning initiative focused on secure coding and defensive engineering practices.


## License

This project is intended for educational and research purposes.
Use responsibly and only in authorized environments.
