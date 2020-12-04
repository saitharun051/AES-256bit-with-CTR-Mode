import socket,pickle,binascii
from pip._vendor.colorama import Fore
from counter.counter import encryption, decryption
message=dict
global c
soc1 = socket.socket()
soc1.bind(('127.0.0.1',5000))
soc1.listen(10)
m=[]
c,addr=soc1.accept()
print("conneced to alice  ",addr)
def encrypt():
    Input = input('enter message to alice: ')
    message = encryption((Input))
    print(Fore.RED+"Ciphertext is : ",binascii.hexlify(message[0]))
    m.append(message[1])
    m.append(message[2])
    data = pickle.dumps(m)
    c.send(message[0])
    c.send(data)
    m.clear()
    message.clear()
def decrypt():
    response1 = c.recv(1024)
    response2 = c.recv(1024)
    resp2 = pickle.loads(response2)
    message1 = decryption(response1, resp2[0], resp2[1])
    print(Fore.WHITE+'Reply from Alice : ', str(message1, 'utf-8') ,"(decrypted text)")
def loop():
    while True:
        encrypt()
        decrypt()
print(Fore.BLUE+"Welcome to the chat")
loop()


