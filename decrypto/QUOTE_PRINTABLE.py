import quopri

def en(s):
    try:
        return quopri.encodestring(s.encode('latin1'))
    except:
        raise Exception("不支持汉字，须先将汉字编码为字节")

def de(s):
    return quopri.decodestring(s).decode('latin1')