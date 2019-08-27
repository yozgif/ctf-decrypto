import base64

def en(s):
    return base64.b32encode(s.encode('latin1')).decode('latin1')


def de(s):
    return base64.b32decode(s.encode('latin1')).decode('latin1')
