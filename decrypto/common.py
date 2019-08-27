import re

# return bytestr.replace(/\\x([0-9a-zA-Z]{2})/g, (_,p1,s)=>String.fromCharCode(parseInt(p1,16)))

def bytestr2str(s):
    return re.sub(r'\\x([0-9a-zA-Z]{2})', lambda x: chr(int(x[1], 16)), s)

def is_dec(s):
    return re.match(r'^[0-9]+$', s)

def is_hex(s):
    return re.match(r'^[0-9a-fA-F]+$', s)