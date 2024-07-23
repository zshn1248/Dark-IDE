from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key)


class __keys__():
    pykey = "9BP0G65juzhuyL4Rs8dwxBHDN14_pL5rdGS6KP6bCqA="
    cppkey = "IevDLeBmwwhTTlwDeZBu4CuRhl0X1N3FGQu8J4oog2I="
    txtkey = "U6a1o8dyfOaSdPS-WksKFPJoOqUbee3Ow77EK5azmKU="
    javakey = "1TE7igNBAgjwbT81ztz2gOYKkmro2dF5RtvsWajvbsk="
def readFile(filename):
    if filename.endswith(".py") == True:
        fernet = Fernet(__keys__.pykey)
        with open(filename, "rb") as file:
            encData = file.read()
        decData = fernet.decrypt(encData)
        return decData.decode()
    elif filename.endswith(".cpp") == True:
        fernet = Fernet(__keys__.cppkey)
        with open(filename, "rb") as file:
            encData = file.read()
        decData = fernet.decrypt(encData)
        return decData.decode()
    elif filename.endswith(".java") == True:
        fernet = Fernet(__keys__.javakey)
        with open(filename, "rb") as file:
            encData = file.read()
        decData = fernet.decrypt(encData)
        return decData.decode()
    else:
        fernet = Fernet(__keys__.txtkey)
        with open(filename+".txt", "rb") as file:
            encData = file.read()
        decData = fernet.decrypt(encData)
        return decData.decode()


def createFile(text, filename):
        text = text.encode()
        
        # with open(original_filename, "rb") as file:
        if filename.endswith(".py") == True:
            fernet = Fernet(__keys__.pykey)
            encData = fernet.encrypt(text)
            with open(filename, "wb") as file:
                file.write(encData)
        elif filename.endswith(".cpp") == True:
            fernet = Fernet(__keys__.cppkey)
            encData = fernet.encrypt(text)
            with open(filename, "wb") as file:
                file.write(encData)
                text = text.encode()
        elif filename.endswith(".java") == True:
            fernet = Fernet(__keys__.javakey)
            encData = fernet.encrypt(text)
            with open(filename, "wb") as file:
                file.write(encData)
        else:
            fernet = Fernet(__keys__.txtkey)
            encData = fernet.encrypt(text)
            with open(filename+".txt", "wb") as file:
                file.write(encData)
            

# createFile("""
# #include <iostream>
# using namespace std;

# int main(){
#     cout << "This is a code edited by Dark" << endl;
#     return 0;
# }
# """, "hello.cpp")
# print(readFile("hello.cpp"))
