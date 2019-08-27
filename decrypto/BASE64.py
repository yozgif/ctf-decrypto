import base64

def en(s):
    return base64.b64encode(s.encode('latin1')).decode('latin1')


def de(s):

    return base64.b64decode(s.encode('latin1')).decode('latin1')
