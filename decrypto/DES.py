from pyDes import *
from . import common

def de(s, key, iv):

    s = common.bytestr2str(s).encode('latin1')
    key = common.bytestr2str(key).encode('latin1')
    iv = common.bytestr2str(iv).encode('latin1')

    d = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    return d.decrypt(s)


