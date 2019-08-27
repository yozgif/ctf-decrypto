def de(e):
    elen = len(e)
    field=[]
    s = ''
    for i in range(2,elen):
        if(elen%i==0):
            field.append(i)

    for f in field:
        b = elen // f
        result = {x:'' for x in range(b)}
        for i in range(elen):
            a = i % b
            result.update({a:result[a] + e[i]})
        d = ''
        for i in range(b):
            d = d + result[i]
        s+='分为 %d 栏时，结果为：  '%(f)+d+'\n'

    return s

en = de