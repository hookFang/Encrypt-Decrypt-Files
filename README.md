# Encrypt-Decrypt-Files

Simple python script to encrypt your files.
All files are encrypted using Fernet -
<h2>AES in Cipher Block Chaining(CBC) mode witha 128-bit key encryption </h2>

# How to Use
    Encrypt Files -> python .\secureFile.py -encrypt "filepath"
    Decrypt Files -> python .\secureFile.py -decrypt "filepath"
    For more info -> python .\secureFile.py --help

    The symmetric key is always stored in the root folder
