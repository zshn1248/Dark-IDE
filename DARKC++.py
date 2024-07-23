from cryptography.fernet import Fernet

# cppkey = Fernet.generate_key()
cppkey = "IevDLeBmwwhTTlwDeZBu4CuRhl0X1N3FGQu8J4oog2I="
# print(cppkey)

def readFile(filename):
    fernet = Fernet(cppkey)
    if filename.endswith(".cpp") == True:
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
        with open(filename+".cpp", "rb") as file:
            encData = file.read()
        decData = fernet.decrypt(encData)
        return decData.decode()


def createFile(text, filename):
        text = text.encode()
        fernet = Fernet(cppkey)
        # with open(original_filename, "rb") as file:
        encData = fernet.encrypt(text)
        if filename.endswith(".cpp") == True:
            with open(filename, "wb") as file:
                file.write(encData)
        else:
            with open(filename+".cpp", "wb") as file:
                file.write(encData)
# createFile("""
# #include <iostream>
# using namespace std;
# int main(){
#     cout << "Hello World" << endl;
#     return 0;
# }
#            """, "hello world.cpp")

print(readFile("hello world.cpp").decode())