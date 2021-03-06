import sys
from os import path
from modules import modulesForSymmetricCryptography
from bcolors import bcolors

def main():
    #we retrive all the arguments
    arguments = len(sys.argv) - 1
    outputArgumentPosition = 1
    if(arguments == 0):
        #Check if the user has any arguments specified
        print(f"{bcolors.FAIL}Please specify the type! For more info type --help{bcolors.ENDC}")
    elif (sys.argv[outputArgumentPosition] == "--help"):
        print("\t How to use SecureFile \n 1. -encrypt \"filepath\" -> To encrypt a file \n 2. -decrypt \"filepath\" -> To decrypt a file \n 3. The Symmetric Keys will always be generated and stored in the root path")
    elif (arguments == 2):
        #If we have two arguments, we then start encryption/decryption
        temp = modulesForSymmetricCryptography()
        #This if statement checks if the user wants to encrypt a file
        if (sys.argv[outputArgumentPosition] == "-encrypt" and bool(sys.argv[outputArgumentPosition + 1])):
            filePath = sys.argv[outputArgumentPosition + 1]
            key_genarted = temp.genrate_key()
            if(key_genarted):
                print(f"{bcolors.OKGREEN}New key created for encryption, starting encryption!{bcolors.ENDC}")
            else:
                print(f"{bcolors.FAIL}Using a previously created key, delete the old the key to craete a new one!{bcolors.ENDC}")
            key = temp.load_key()
            if(path.exists(filePath)):
                temp.encrypt(filePath, key)
                print(f"{bcolors.OKGREEN}File successfully encrypted and stored at {filePath}{bcolors.ENDC}" )
        #Decrypting a file
        elif (sys.argv[outputArgumentPosition] == "-decrypt" and bool(sys.argv[outputArgumentPosition + 1])):
            filePath = sys.argv[outputArgumentPosition + 1]
            key = temp.load_key()
            if(path.exists(filePath)):
                temp.decrypt(filePath, key)
    else:
        print(f"{bcolors.FAIL}Please specify the type! For more info type --help{bcolors.ENDC}")

if __name__ == "__main__":
    main()

