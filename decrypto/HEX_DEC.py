def en(s, p):
    if not p:
        p = ' '
    
    def dec2hex(m):
        r = hex(int(m))[2:]
        if len(r)%2 == 0:
            return r
        else:
            return '0'+r
   
    s = [x for x in s.strip().split(p) if x]
    return p.join(map(dec2hex, s))

def de(s, p):
    if not p:
        p = ' '
        
    s = [x for x in s.strip().split(p) if x]
    return p.join(map(lambda x: str(int(x.strip(), 16)), s))

