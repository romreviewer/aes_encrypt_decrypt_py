#author RomReviewer
import os
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
from Cryptodome.Util.Padding import unpad
from base64 import b64decode
import json
from base64 import b64encode
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
config=open(os.path.join(__location__,"config.json"),"r")
js=json.loads(config.read())
iv=str.encode(js["iv"])
key=str.encode(js["key"])
def encrypt():
    f = open(os.path.join(__location__,"input.txt"), "r")
    data = str.encode(str(f))
    cipher = AES.new(key, AES.MODE_CBC,iv)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    ct = b64encode(ct_bytes).decode('utf-8')
    w=open(os.path.join(__location__,"output.txt"),"a")
    w.truncate(0)
    w.write(ct)
    print("Encryption Successful")
def decrypt():
    try:
        f = open(os.path.join(__location__, "input.txt"), "r")
        ct = b64decode(f.read())
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        w=open(os.path.join(__location__,"output.txt"),"a")
        w.truncate(0)
        w.write(pt.decode('utf-8'))
        print("Decryption Successful")
    except ValueError:
        print("Incorrect decryption")    
def chooser():
    c=int(input("Please Select desired choice :- \n1:- Encrypt\n2:- Decrypt\n"))
    if(c==1):
        encrypt()
    elif(c==2):
        decrypt()
    else:
        print("Invalid Input!")
        chooser()
chooser()