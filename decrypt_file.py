#Import the cryptography library
from cryptography.fernet import Fernet
from load_key import load_key

def decrypt(filename, key):
    f = Fernet(key)
    file = open(filename, "rb")
    if file.mode == 'rb':
        print("we are here")
        encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        newFile = open("decrypted.txt", "wb")
        newFile.write(decrypted_data)

#Load the key and pass it into the function
key = load_key()
decrypt("encrypted.txt", key)