import binascii

def en(s):
    s = s.replace(' ','')
    return binascii.unhexlify(s).decode('latin1')
    
    # return ''.join([chr(int(s[i*2:i*2+2],16)) for i in range(len(s)//2)])


def de(s):
    s = s.replace(' ','')
    return binascii.hexlify(s.encode('latin1'))