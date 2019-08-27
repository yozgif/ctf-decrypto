import base65536

def en(s):
    return base65536.encode(s.encode('latin1'))

def de(s):
    return base65536.decode(s).decode('latin1')