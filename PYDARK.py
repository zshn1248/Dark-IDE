from cryptography.fernet import Fernet

# pykey = Fernet.generate_key()
pykey = "9BP0G65juzhuyL4Rs8dwxBHDN14_pL5rdGS6KP6bCqA="
# print(pykey)

def readFile(filename):
    fernet = Fernet(pykey)
    if filename.endswith(".py") == True:
        """
        Decrypt file
        filename: encrypted filename
        save_as: filename to save decrypted file
        keyfile: filename of key used for encryption
        """
        
        with open(filename, "rb") as file:
            encData = file.read()
        decData = fernet.decrypt(encData)
        return decData
    else:
        with open(filename+".py", "rb") as file:
            encData = file.read()
        decData = fernet.decrypt(encData)
        return decData.decode()


def createFile(text, filename):
        text = text.encode()
        fernet = Fernet(pykey)
        # with open(original_filename, "rb") as file:
        encData = fernet.encrypt(text)
        if filename.endswith(".py") == True:
            with open(filename, "wb") as file:
                file.write(encData)
        else:
            with open(filename+".py", "wb") as file:
                file.write(encData)


# createFile("""
# import pandas as pd
# import numpy as np

# print("every thing loaded)
# """, "loader")

print(readFile("loader"))