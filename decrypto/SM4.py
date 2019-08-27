from sm4 import SM4Key
from . import common


def en(data, key):
    data = common.bytestr2str(data).encode('latin1')
    key = common.bytestr2str(key).encode('latin1')
    sm4 = SM4Key(key)  # key, 16 bytes
    return sm4.encrypt(data).decode('latin1')  # 解密

def de(data, key):

    data = common.bytestr2str(data).encode('latin1')
    key = common.bytestr2str(key).encode('latin1')
    sm4 = SM4Key(key)
    return sm4.decrypt(data).decode('latin1')
