'''
Decrypts files with Encrypt.py and keys generated with keygen.py - by don-batista!
RSA!
'''
import rsa
import sys
from cryptography.fernet import Fernet


def decryptFile(edata, cipher):
    decrypted_data = cipher.decrypt(edata)
    em = decrypted_data.decode()
    
    return decrypted_data, em
def importKeys(pkey, ekey):
    try:
        private_key = rsa.PrivateKey.load_pkcs1(pkey)
    except:
        print("Error loading privateKey, it is probably not a private key"!)

    try:
        dpubkey = rsa.decrypt(ekey, private_key)
    except:
        print("Error decrypting key!")

    try:
        cipher = Fernet(dpubkey)
    except:
        print("Error generating the cipher!")
        sys.exit()

    return private_key, dpubkey, cipher
def main():
    ##Abrindo arquivo que será criptografado
    fileu = str(input("File: "))
    ##Abrindo a chave privada RSA
    prkey = open('keys/privKey', 'rb')
    pkey = prkey.read()
    
    #Abrindo a chave cifrada
    e = open('keys/encrypted_key', 'rb')
    ekey = e.read()
    private_key, dpubkey, cipher = importKeys(pkey, ekey)

    encrypted_data = open(fileu, 'rb')
    edata = encrypted_data.read()

    decrypted_data, em = decryptFile(edata, cipher)
    encrypted_data.close()
    ou = open(fileu, 'w')
    print('Decrypted!')
    ou.write(str(em))

if __name__ == "__main__":
    main()
