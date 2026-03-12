# Cryptographic File Protector

## Project Overview

The Secure File Encryption & Decryption Tool is a command-line cybersecurity application developed in Python to protect sensitive digital information using modern cryptographic techniques.

The system showcases practical implementation of secure data protection mechanisms such as password-based key generation, authenticated symmetric encryption, and integrity validation. It simulates the workflow of real-world secure storage utilities that are designed to prevent unauthorized access to confidential files.

By combining encryption, hashing, and verification processes, the tool demonstrates how layered security controls can be used to maintain both data confidentiality and authenticity.


## Key Capabilities

* Strong file encryption using authenticated symmetric cryptography
* Encryption keys generated securely from user passwords
* Dynamic random salt creation for enhanced security
* Integrity verification using SHA-256 hashing
* Detection of incorrect passwords during decryption
* Identification of altered or corrupted encrypted data
* Interactive terminal-based user interface
* Compatible across different operating systems


## Cryptographic Principles Demonstrated

This project reflects applied cybersecurity engineering concepts, including:

* Password-derived key generation using PBKDF2-HMAC
* Secure randomization through salt values
* Authenticated encryption ensuring confidentiality and authenticity
* Hash-based validation to confirm file integrity
* Structured storage of encrypted data components

These mechanisms collectively represent foundational practices used in encrypted storage systems and secure data vault implementations.

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


## Security Significance

The tool highlights defensive cybersecurity development practices by:

* Restricting unauthorized access to protected files
* Enabling detection of tampering or integrity compromise
* Applying recognized cryptographic standards
* Maintaining both confidentiality and verification controls
* Demonstrating secure software design thinking



## Performance Considerations

* Efficient handling of large files through chunk-based hashing
* Lightweight encryption suitable for local execution environments
* Optimized password-based key derivation process
* Low system resource consumption during operations


## Responsible and Ethical Usage

This project is designed strictly for educational and research purposes such as:

* Cybersecurity skill development
* Secure coding practice
* Applied cryptography experimentation
* Defensive security tool design

It must not be used to conceal or facilitate unlawful activities.


## Learning Outcomes

Development of this tool demonstrates understanding of:

* Practical cryptography implementation
* Secure password and key handling strategies
* File validation and integrity assurance techniques
* Defensive software engineering methodologies
* Secure data protection architecture
* Building functional cybersecurity utilities


## Author

This project was created as part of a hands-on cybersecurity learning journey aimed at strengthening secure programming skills and defensive engineering awareness.


## License

Provided for educational and research use.
Users are expected to apply this tool responsibly within authorized environments.
