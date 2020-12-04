import pyaes, pbkdf2, binascii, os, secrets
def encryption(p):
    password = "/dgdhft*hfhd3"
    passwordSalt = os.urandom(16)
    key = pbkdf2.PBKDF2(password, passwordSalt).read(32)
    p1=[]
    p1.clear()
    iv = secrets.randbits(256)
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    ciphertext = aes.encrypt(p)
    p1.append(ciphertext),p1.append(key),p1.append(iv)
    return p1
def decryption(c,k,iv):
    aes = pyaes.AESModeOfOperationCTR(k, pyaes.Counter(iv))
    decrypted = aes.decrypt(c)
    return decrypted

