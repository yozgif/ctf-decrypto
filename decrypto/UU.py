
import codecs
def en(s):
    return codecs.encode(s.encode('latin1'), 'uu')[17:-7].decode('latin1')

def de(s):
    s = b'begin 666 <data>\n' + s.encode('latin1') + b'\n \nend\n'
    return codecs.decode(s, 'uu').decode('latin1')

