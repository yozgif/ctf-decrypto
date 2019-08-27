### 自用CTF加解密工具
结合CyberChef可以解决大部分CTF加解密，如果解决不了...那就添加进来

### 安装
本程序适用于Python3

`pip3 install -r requirement.txt`

### 使用
`python3 run.py`

浏览器访问 `127.0.0.1`

### 用法提示
1. 输入支持\xff形式，也支持无法打印的\xff乱码
2. 字符运算可用于逆向中的异或/ascii偏移等情况

### 开发指南
每添加一项编解码，需要修改的有：
1. list.json (用于在前端显示)
    - id: 英文
    - name：前端显示名称
    - class: 实现方式， python / js / str
    - para： 参数名，多个参数用`,`分隔
    - default_para：参数提示，多个参数用`,`分隔
    - hint：说明和帮助
2. 如果是python实现，decrypto中添加id同名py，实现en,de
3. 如果是js实现，static中添加id同名js，实现id_en, id_de ；`index.html` header中添加static/js实现路径
4. str相关函数在`static/content.js/str_template`中实现

### 安全事项
**不要**将端口开放到互联网中，后端为方便起见用到了eval函数，不保证安全性。(大佬可以尝试getshell，甚至拿来出道题)

### TO-DO
1. paras label和input在同一行，自适应宽度
2. 添加按钮复制到粘贴板