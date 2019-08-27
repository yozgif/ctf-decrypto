function Vigenere (strIn, key, encode) {
    this.charOffset = function(char, offset) {
        if (offset < 0)
            offset += 26;
        if(/[a-z]/.test(char)) {
            return String.fromCharCode((char.charCodeAt(0)-97+offset)%26+97);
        }else {
            return String.fromCharCode((char.charCodeAt(0)-65+offset)%26+65);
        }
    }


    var strOut = "";
    var j=0;   //  j 对应密钥key；
    for (var i = 0; i < strIn.length; i++) {
        var c = strIn[i];
        if( /[a-zA-Z]/.test(c) ){
            var offset = key.charCodeAt( j%key.length ) - 97;
            j++;
            if(encode == false)offset = -offset;
            strOut += this.charOffset(c, offset);
        }else {
            strOut += c;
        }
    }
    return strOut;
}
function vigenere_en(data) {
    // body...

    var method = data['method'];
    var s = data['s'];
    var paras = JSON.parse(data['paras']);
    var key = paras[0].toLowerCase();
    var key_len = paras[1];

    if(!key) {
        if (method == 'en')
            return "请输入密钥";
        else
            key = Vigenere_calkey(s, key_len);
            $($('.paras input')[0]).val(key);
    }

    return Vigenere(s, key, 'en'==method);

}

vigenere_de = vigenere_en;

function Vigenere_calkey (ciphertext, best_len) {
    var best_len = parseInt(best_len);
    var best_key = "";
    var count = [];
    var cipherMin = ciphertext.toLowerCase().replace(/[^a-z]/g, "");
    var freq = [8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074];
    if(!best_len) {
        for(var best_len = 3; best_len < 13; best_len++) {  //猜测key长度3————12
            var sum = 0;
            for (var j = 0; j < best_len; j++) {
                for (var i=0; i<26; i++) {
                    count[i] = 0;
                }
                for (var i = j; i < cipherMin.length; i+=best_len) {
                    count[cipherMin[i].charCodeAt(0)-97] += 1;
                }
                var ic = 0;
                var num = cipherMin.length/best_len;
                for (var i = 0; i < count.length; i++) {
                    ic += Math.pow(count[i]/num,2);
                }
                sum += ic;
                // console.log(keyLen,ic);
            }console.log(sum/best_len);
            if(sum/best_len > 0.065)break;  //确定密钥长度
        }
    }

    for (var j = 0; j < best_len; j++) {
        for (var i=0; i<26; i++) {
            count[i] = 0;
        }
        for (var i = j; i < cipherMin.length; i+=best_len) {
            count[cipherMin[i].charCodeAt(0)-97] += 1;
        }
        var max_dp = -1000000;
        var best_i = 0;

        for (var i = 0; i < 26; i++) {
            var cur_dp=0.0;
            for (var k = 0; k < 26; k++) {
                cur_dp += freq[k]*count[(k+i)%26];//这里要找出频率分布匹配的key
            }
            if (cur_dp > max_dp) {
                max_dp = cur_dp;
                best_i = i;
            }
        }
        best_key += String.fromCharCode(best_i+97);
    }
    return best_key;
}
