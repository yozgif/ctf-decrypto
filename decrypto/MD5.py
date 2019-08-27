import hashlib


def en(s):
    m = hashlib.md5()
    m.update(s.encode('latin1'))
    return m.hexdigest()
