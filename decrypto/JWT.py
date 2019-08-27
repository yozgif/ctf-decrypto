import jwt
import json
import base64

def en(s, key, al):
    if al == "":
        al = "HS256"
    return jwt.encode(json.loads(s), key, algorithm=al).decode('latin1')

def de(s, key, al):
    if al == "":
        al = "HS256"

    header, payload, _ = s.split('.')
    header = base64.urlsafe_b64decode(header+'==').decode('latin1')
    payload = base64.urlsafe_b64decode(payload+'==').decode('latin1')
    try:
        json.dumps(jwt.decode(s, key, al))
    except Exception as e:
        ret = '验证失败，key 不对'
    else:
        ret = '验证成功，key 正确'

    return 'header: %s\r\npayload: %s\r\n%s'%(header, payload, ret)