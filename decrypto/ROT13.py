import codecs

def en(s):
    return codecs.encode(s, "rot-13")

def de(s):
    return codecs.decode(s, "rot-13")