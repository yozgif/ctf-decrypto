from flask import Flask, render_template, request
from decrypto import *
import json
import re
import os

app = Flask(__name__)
json_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'list.json')
j = json.load(open(json_file, encoding='utf-8'))

@app.route('/')
def new():
    return render_template('index.html', j=j)

@app.route('/process', methods=['POST'])
def process():
    data = request.values
    s = re.sub(r'\\x([0-9a-zA-Z]{2})', lambda x: chr(int(x[1], 16)), data['s'])
    encrypt = data['encrypt']
    method = data['method']
    paras = json.loads(data['paras'])
    if method not in ('en','de'):
        return
    try:
        exp = encrypt+'.'+method+'(s, *paras)'
        ret = eval(exp)
    except AttributeError:
        trans = {'en': "编码", 'de': '解码'}
        ret = '[错误] {0} 不支持 {1}'.format(encrypt, trans[method])
    except Exception as e:
        ret = str(e)

    return ret


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=80)
