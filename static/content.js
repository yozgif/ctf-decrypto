function Unicode_de(data){
    var s = eval('"'+$('#text').text()+'"');
    return s;
}




function print_ret(data){
    $("#ret").text(data);
    if($('#auto_swp_in_out').get(0).checked){
        $('#swp_in_out').click();
    }
}

function set_label(ar, default_para){
    var a, b, c, l = ar.length;
    var t = [];
    for(i=0;i<l;i++){
        b = '#para'+i+' label';
        t.push($(b) && $(b).text()==ar[i]+': ');
    }
    if(t.some(x=>x)) return false;

    $('.paras').text("");
    for(i=0;i<l;i++){
        a = '<div id="para'+i+'"><label class="control-label"></label><input class="form-control"></div>';
        $('.paras').append(a);
        b = '#para'+i+' label';
        $(b).text(ar[i]+': ');
        b = '#para'+i+' input';
        $(b).attr("placeholder", default_para[i])
    }
    return true;
}

function pre_data_process(dom_button){
    const method_dict = {'编码':'en', '解码':'de'};
    var encrypt = $(dom_button).attr("id");
    var s = $('#text').text();
    var method = method_dict[$("#method").text()];


    var hint = $(dom_button).attr("hint");
    var label = $(dom_button).attr("paras");
    var paras = [];

    $('#hint').text(hint);
    if(label){ //have paras
        label = label.split(',')
        var default_para = $(dom_button).attr("default_para").split(',');
        if(set_label(label, default_para)) return false;   //just set label
        for(i=0; i<label.length; i++){
            var t = $($('.paras input')[i]).val();
            paras.push(t);
        }
    }else
        $('.paras').text("");

    if(!s) return false;

    return {"s": s, "encrypt": encrypt, "method": method, "paras":JSON.stringify(paras)};

}

function post_data(){
    var data = pre_data_process(this);
    if(!data) return;
    $.ajax({
        type: 'POST',
        url:"/process",
        data:data,
        success: function(data){
            print_ret(data);
        }
    });
}

function bytestr2str(bytestr){
    // \\x12 -> \x12
    return bytestr.replace(/\\x([0-9a-zA-Z]{2})/g, (_,p1,s)=>String.fromCharCode(parseInt(p1,16)))
}

function js(){
    var data = pre_data_process(this);
    if(!data) return;

    var encrypt = data['encrypt'];
    var hint = $(this).attr("hint");
    var function_name;

    $('#hint').text(hint);
    if($("#method").text() == '解码'){
        function_name = encrypt+'_de';
    }else{
        function_name = encrypt+'_en';
    }
    try{
        if(typeof(eval(function_name))=="function")
            s = eval(function_name)(data);
            print_ret(s);
    }catch(ReferenceError){
        print_ret("不支持"+$("#method").text());
    }
}

function str_template(){

    var data = pre_data_process(this);
    if(!data) return;
    var encrypt = data['encrypt'];
    var s = data['s'];
    var paras = JSON.parse(data['paras']);
    var p1 = paras[0];
    var p2 = paras[1];


    const str_reverse = s => s.split('').reverse().join('');
    const str_up_low  = s => s = '小写：'+s.toLowerCase()+'\r\n'  + '大写：'+s.toUpperCase()
    const str_replace = s => s.replace(new RegExp(p1, 'g'), p2);
    const str_split   = s => {
        p1 = parseInt(p1);
        var tmp = '';
        if (p2 == "") p2 = " ";
        for(var i=0; i<Math.ceil(s.length/p1); i++)
            tmp += p2 + s.slice(i*p1, i*p1+p1);

        return tmp;
    };

    const str_calc    = s => {
        s = bytestr2str(s).split('').map((x,i)=>eval(String(x.charCodeAt())+p1));
        return String.fromCharCode(...s);};

    s = eval(encrypt)(s);
    print_ret(s);
}

function str2bytes (str) {
    var bytes = new Uint8Array(str.length);
    for (var i=0; i<str.length; i++) {
        bytes[i] = str.charCodeAt(i);
    }
    return bytes;
}

$(document).ready(function(){

    function get_text_length (){
        var l = String($('#text').text().length);
        $("#length").text(l);
    }

    //编解码切换
    $("#method").click(function(){
        var a = $(this).text()=='编码' ? '解码' : "编码";
        $(this).text(a);
    });

    $("#save_out").click(function(){
        var data = $("#ret").text();
        if (data.length){
            var blob = new Blob([str2bytes(data)], {type: "application/octet-stream"});
            saveAs(blob, "imported_file");
        }
    });


    $('#text').keyup(get_text_length);

    $('#swp_in_out').click(function(){
        var tmp = $('#text').text();
        $("#text").text($("#ret").text());
        $("#ret").text(tmp);
        get_text_length();
    });

    $('#swp_out_tmp').click(function(){
        var tmp = $('#ret').text();
        $("#ret").text($("#tmp").text());
        $("#tmp").text(tmp);
    });





    $(".btn-default").click(function(){
        $(".active").removeClass("active");
        $(this).addClass("active");
    });

    $(".str").click(str_template);
    $(".js").click(js);
    $(".python").click(post_data);

});