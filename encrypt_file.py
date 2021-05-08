#Import the cryptography library
from cryptography.fernet import Fernet
from load_key import load_key

def encrypt(filename, key):
    f = Fernet(key)
    file = open(filename, "rb")
    if file.mode == 'rb':
        print("we are here")
        content = file.read()
        encrypted_data = f.encrypt(content)
        newFile = open("encrypted-decrypted-files/encrypted.txt", "wb")
        newFile.write(encrypted_data)

#Load the key and pass it into the function
key = load_key()
encrypt("textFile.txt", key)