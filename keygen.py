'''
RSA Keygenerator for other scripts - by carmine-falcone!
RSA KEYS!
'''
#Modules
import rsa
import os
from cryptography.fernet import Fernet

#Vars
panel = '''
Bits          Security Level        Qualification        How much security time           Symmetric key equivalent             Ob
1024             Very low             Breakable       Between 2006-2010 it becomes breakable        82                      DO NOT USE!
2048              Normal             Hard to break       It will be enough by 2030                  112                      Safe!
3072              SAFE                Unbreakable              After 2030                           128                     Very SAFE!!!
15360           UNBREAKABLE         NSA(Unbreakable)          Very after 2030                       256                     Completely SAFE!!!!!!
'''

def RSAKeyGenerator():
    print(panel)
    bits = int(input("Bits: "))
    print("Generating RSA Keys!!!")
    (pub_key,priv_key)=rsa.newkeys(bits)
    print("Finish!")
    return pub_key, priv_key

def main():
    key = Fernet.generate_key()
    try:
        k = open("keys/symmetric.key", 'wb')
    except:
        os.mkdir("keys")
        k = open("keys/symmetric.key", 'wb')
    k.write(key)
    k.close()
    pub_key, priv_key = RSAKeyGenerator()

    print("Saving Keys!")
    pkey = open("keys/publickKey", 'wb')
    pkey.write(pub_key.save_pkcs1('PEM'))
    pkey.close()

    prkey = open("keys/privKey", 'wb')
    prkey.write(priv_key.save_pkcs1('PEM'))
    prkey.close()
    print("Saved!")
if __name__ == "__main__":
    main()
