import pickle,socket,binascii
from pip._vendor.colorama import Fore
from counter.counter import encryption, decryption
msg=[]
m=[]
soc2 = socket.socket()
soc2.bind(('127.0.0.1',5001))
soc2.connect(('127.0.0.1',5000))
def sock():
    loop()
def encrypt():
    Input = input('enter message to bob :')
    msg =encryption((Input))
    print(Fore.RED,"Ciphertext is : ", binascii.hexlify(msg[0]))
    m.append(msg[1])
    m.append(msg[2])
    data = pickle.dumps(m)
    soc2.send(msg[0])
    soc2.send(data)
def decrypt():
    m.clear()
    msg.clear()
    response1 = soc2.recv(1024)
    response2 = soc2.recv(1024)
    resp2 = pickle.loads(response2)
    message = decryption(response1, resp2[0], resp2[1])
    print(Fore.WHITE+'Message from Bob : ', str(message, 'utf-8') ,"(decrypted text)")
def loop():
    while True:
        decrypt()
        encrypt()
print(Fore.BLUE+ "Welcome to the chat ")
sock()