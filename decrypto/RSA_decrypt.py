from Crypto.Util.number import *
from . import common


def de(data, p, q, e):
    if common.is_dec(data):
        data = int(data)
    elif common.is_hex(data):
        data = int(data, 16)
    else:
        data = bytes_to_long(data)

    if common.is_dec(p) and common.is_dec(q):
        p = int(p)
        q = int(q)
    elif common.is_hex(p) and common.is_hex(q):
        p = int(p, 16)
        q = int(q, 16)
    else:
        raise Exception('输入十进制或16进制')

    if e == '':
        e = 65537

    d = inverse(e, (p-1)*(q-1))
    s = pow(data, d, p*q)
    return str(s)
