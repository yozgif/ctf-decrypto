import chardet


def en(s, encoding):
    return str(s.encode(encoding))[2:-1]

def de(s, encoding):
    try:
        b = s.encode('latin1')
        if encoding == '':
            encoding = chardet.detect(b)['encoding']
        return b.decode(encoding)
    except:
        raise Exception("字节->字符失败，确保输入区是字节数据")