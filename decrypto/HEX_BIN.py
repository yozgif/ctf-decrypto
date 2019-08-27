def de(s):
    s = s.replace(' ','')
    return ''.join(['%04d'%int(bin(int(j,16))[2:]) for j in s])

def en(s):
    s = s.replace(' ','')
    if(len(s) % 4):
        raise Exception("输入二进制个数应该是4的整数倍")
    
    h = [hex(int(s[i*4 : i*4+4], 2))[-1] for i in range(len(s)//4)]
    return ''.join(h)