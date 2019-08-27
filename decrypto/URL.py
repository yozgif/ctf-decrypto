import urllib.parse

def en(s):
    try:
        return urllib.parse.quote(s, encoding='latin1')
    except:
        raise Exception("仅支持字母、数字、特殊字符的编码，汉字可以在字符<->字节编码后将\\x转为%")

def de(s):
    return urllib.parse.unquote(s, encoding='latin1')