#Import the cryptography library
from cryptography.fernet import Fernet
from os import path

class modulesForSymmetricCryptography():
    def encrypt(self, filename, key):
        f = Fernet(key)
        file = open(filename, "rb")
        if file.mode == 'rb':
            content = file.read()
            encrypted_data = f.encrypt(content)
            newFile = open(filename, "wb")
            newFile.write(encrypted_data)

    def decrypt(self, filename, key):
        f = Fernet(key)
        file = open(filename, "rb")
        if file.mode == 'rb':
            encrypted_data = file.read()
            decrypted_data = f.decrypt(encrypted_data)
            newFile = open(filename, "wb")
            newFile.write(decrypted_data)

    def load_key(self):
        return open("symmetricKey.key", "rb").read()

    def genrate_key(self):
        key = Fernet.generate_key()
        if(not path.exists("symmetricKey.key")):
            symmetric_key = open("symmetricKey.key", "wb")
            symmetric_key.write(key)
            return 1
        return 0
