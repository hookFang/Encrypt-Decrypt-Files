#Import the cryptography library
from cryptography.fernet import Fernet

#We genaret a symmetric key that is going to be used for enecrypting and decrypting the files
def genrate_key():
    key = Fernet.generate_key()
    with open("symmetricKey.key", "wb") as key_file:
        key_file.write(key)

genrate_key()