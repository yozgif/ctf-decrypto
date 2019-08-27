import binascii

def de(s):
    s = s.replace(' ','')
    return binascii.unhexlify(s).decode('latin1')


def en(s):
    s = s.replace(' ','')
    return binascii.hexlify(s.encode('latin1'))