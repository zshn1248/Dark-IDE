from cryptography.fernet import Fernet

key = "1TE7igNBAgjwbT81ztz2gOYKkmro2dF5RtvsWajvbsk="
def readFile(filename):
    if filename.endswith(".java") == True:
        fernet = Fernet(key)
        with open(filename, "rb") as file:
            encData = file.read()
        decData = fernet.decrypt(encData)
        return decData.decode()
    else:
        fernet = Fernet(key)
        with open(filename+".java", "rb") as file:
            encData = file.read()
        decData = fernet.decrypt(encData)
        return decData.decode()
def createFile(text, filename):
        text = text.encode()
        if filename.endswith(".java") == True:
            fernet = Fernet(key)
            encData = fernet.encrypt(text)
            with open(filename, "wb") as file:
                file.write(encData)
        else:
            fernet = Fernet(key)
            encData = fernet.encrypt(text)
            with open(filename+".java", "wb") as file:
                file.write(encData)
