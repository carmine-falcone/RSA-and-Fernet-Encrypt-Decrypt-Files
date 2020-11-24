'''
Encrypt files with keys generated with keygen.py - by don-batista!
RSA!
'''
#Modules
from cryptography.fernet import Fernet
import rsa
import sys

#Vars
panel = '''
Bits          Security Level        Qualification        How much security time           Symmetric key equivalent             Ob
1024             Very low             Breakable       Between 2006-2010 it becomes breakable        82                      DO NOT USE!
2048              Normal             Hard to break       It will be enough by 2030                  112                      Safe!
3072              SAFE                Unbreakable              After 2030                           128                     Very SAFE!!!
15360           UNBREAKABLE         NSA(Unbreakable)          Very after 2030                       256                     Completely SAFE!!!!!!
'''

def EncryptFile(cipher, myfiledata, fileu):
    encrypted_data = cipher.encrypt(myfiledata)
    edata = open(fileu, 'wb')
    edata.write(encrypted_data)
    return encrypted_data

def importkeys(symmetricKey, publickKey, encrypt_key):
    ##Symmetric Key
    while 1:
            try:
                skey = open(symmetricKey, 'rb')
                break
            except FileNotFoundError:
                print("File symmetricKey not found!")
                symmetricKey = str(input("SymmetricKey: "))

    key = skey.read()
    try:
        cipher = Fernet(key)
    except:
        print("Error creating cipher from SymmetricKey, try to generate another error!")

    #RSA Key
    while 1:
        try:
            pkey = open(publickKey, 'rb')
            break
        except FileNotFoundError:
            print("File publicKey not found!")
            publickKey = str(input("PublicKey: "))
    pkdata = pkey.read()

    try:
        pubkey = rsa.PublicKey.load_pkcs1(pkdata)
    except:
        print("Error loading publicKey, try to generate another valid one!")

    try:
        encrypted_key = rsa.encrypt(key,pubkey)
        ekey = open(encrypt_key, 'wb')
        ekey.write(encrypted_key)
        ekey.close()

    except:
        print("Error while encrypting the key!")
        sys.exit()
    
    return cipher, pubkey, encrypted_key

def main():
    cipher, pubkey, encrypted_key = importkeys('keys/symmetric.key', 'keys/publickKey', "keys/encrypted_key")

    fileu = str(input("File:"))
    myfile = open(fileu, 'rb')
    myfiledata = myfile.read()
    encrypted_data = EncryptFile(cipher, myfiledata, fileu)
    
    wow = str(input("Do you want to see the encrypted content and the encrypted key? [Y/N]?"))
    if wow.upper() == 'Y':
        print(encrypted_data)
        print(encrypted_key)
        print("Finished!")
    else:
        print("Finished!")

if __name__ == "__main__":
    main()
