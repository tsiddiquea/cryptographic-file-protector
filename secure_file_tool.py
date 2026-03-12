import os
import base64
import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


# ---------------------------
# Key Derivation Function
# ---------------------------
def generate_key_from_password(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))


# ---------------------------
# SHA-256 File Hash
# ---------------------------
def get_file_hash(filename):
    sha256 = hashlib.sha256()
    with open(filename, "rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()


# ---------------------------
# Encrypt Function
# ---------------------------
def encrypt_file(filename):
    if not os.path.exists(filename):
        print("File does not exist.")
        return

    password = input("Enter password: ")
    salt = os.urandom(16)

    key = generate_key_from_password(password, salt)
    fernet = Fernet(key)

    original_hash = get_file_hash(filename)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted_data = fernet.encrypt(data)

    encrypted_filename = filename + ".enc"

    with open(encrypted_filename, "wb") as file:
        file.write(salt)
        file.write(original_hash.encode())  # store hash
        file.write(encrypted_data)

    print("\nFile encrypted successfully.")
    print("Encrypted file:", encrypted_filename)
    print("Integrity hash stored securely.")


# ---------------------------
# Decrypt Function
# ---------------------------
def decrypt_file(filename):
    if not os.path.exists(filename):
        print("File does not exist.")
        return

    password = input("Enter password: ")

    with open(filename, "rb") as file:
        salt = file.read(16)
        stored_hash = file.read(64).decode()
        encrypted_data = file.read()

    key = generate_key_from_password(password, salt)
    fernet = Fernet(key)

    try:
        decrypted_data = fernet.decrypt(encrypted_data)
    except Exception:
        print("Wrong password or corrupted file.")
        return

    decrypted_filename = filename.replace(".enc", "_decrypted")

    with open(decrypted_filename, "wb") as file:
        file.write(decrypted_data)

    decrypted_hash = get_file_hash(decrypted_filename)

    print("\nFile decrypted successfully.")

    if decrypted_hash == stored_hash:
        print("Integrity Verified: File is authentic.")
    else:
        print("Warning: Integrity compromised!")

    print("Decrypted file:", decrypted_filename)


# ---------------------------
# Main Program
# ---------------------------
def main():
    print("Secure File Encryption Tool")
    print("1. Encrypt File")
    print("2. Decrypt File")

    choice = input("Choose option (1/2): ")

    if choice == "1":
        filename = input("Enter file name to encrypt: ")
        encrypt_file(filename)

    elif choice == "2":
        filename = input("Enter file name to decrypt: ")
        decrypt_file(filename)

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()