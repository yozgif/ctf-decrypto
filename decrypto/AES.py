from Crypto.Cipher import AES
from . import common

def en(data, key, iv):
    data = common.bytestr2str(data).encode('latin1')
    key = common.bytestr2str(key).encode('latin1')
    iv = common.bytestr2str(iv).encode('latin1')

    bs = AES.block_size

    # PKCS#5 / PKCS#7
    pad = lambda s: s + (bs - len(s) % bs) * bytes(bytearray([bs - len(s) % bs]))
    
    if iv:
        cipher = AES.new(key, AES.MODE_CBC, iv)
    else:
        cipher = AES.new(key, AES.MODE_ECB)
    
    data = cipher.encrypt(pad(data))
    return data.decode('latin1')

def de(data, key, iv):
    data = common.bytestr2str(data).encode('latin1')
    key = common.bytestr2str(key).encode('latin1')
    iv = common.bytestr2str(iv).encode('latin1')
    

    if iv:
        unpad = lambda s: s[0:-s[-1]]  # PKCS#5 / PKCS#7
        cipher = AES.new(key, AES.MODE_CBC, iv)
        data = unpad(cipher.decrypt(data))
    else:
        cipher = AES.new(key, AES.MODE_ECB)
        data = cipher.decrypt(data)
    
    return data.decode('latin1')
    
if __name__ == "__main__":
    
    data = b'\xf0\x85\xd6\x69\xa7\x6c\x86\xde\x59\xeb\x3e\x3f\x6e\x39\x77\x5d'
    key = b'\x33\x89\x25\x46\x28\xae\xd2\xa6\xab\xf7\x15\x28\x39\x4f\x5f\x6c'
    

    # unpad = lambda s: s[0:-s[-1]]

    cipher = AES.new(key, AES.MODE_ECB)
    data = (cipher.decrypt(data))
    print(data)