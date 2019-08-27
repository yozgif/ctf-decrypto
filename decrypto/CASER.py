import string
def en(s, n):
    n = int(n)
    return s.translate(str.maketrans(string.ascii_uppercase + string.ascii_lowercase,
        string.ascii_uppercase[n:] + string.ascii_uppercase[:n] +
        string.ascii_lowercase[n:] + string.ascii_lowercase[:n]))
        

def de(s, n):
    n = int(n)
    return en(s, -n)
    
    