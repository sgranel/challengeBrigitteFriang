var _0x5f46 = ['7<0l<ni03<l<l<3>5<b`>dk>j;3n0>>o9n0`nk39', '9o#jzQ$=W8sN>n?kIXuIM7sh6 WilbDPx`1&YF5z', 'length', 'split', 'charAt', 'join', 'd[cn?k+qje)/N|t.wkGr]rO+k9b=2y,}@Zyb:8pla2\'6%dn)', 'charCodeAt', 'fromCharCode'];
var _0x19fd = function (arg1, arg2) {
    arg1 = arg1 - 0;
    var _0x79ddde = _0x5f46[arg1];
    return _0x79ddde;
};

function startProg(_0x1975bf) {
    var const1 = '7<0l<ni03<l<l<3>5<b`>dk>j;3n0>>o9n0`nk39'
    var check = 0;
    var checkedVal = _0x4bf1ad(_0x53e54e(_0x1975bf));
    if (checkedVal == const1) {
        check = 1;
    } else {
        check = 0;
    }
    return check;
}

function _0x33903e(arg1) {
    var const_array = [2, 21, 0, 34, 11,9, 23, 30, 14, 5, 29, 4, 24, 22, 8, 20, 31, 17, 38, 35, 15, 1, 13, 6, 12, 26, 25, 27, 33, 10, 7, 16, 32, 28, 3, 19,37, 36, 18, 39];
    var const1 = '9o#jzQ$=W8sN>n?kIXuIM7sh6 WilbDPx`1&YF5z';
    var cpt = 0;
    var sizeMax = const1['length'];
    while (arg1['length'] < 40) {
        arg1 += const1[cpt++];
        if (cpt >= sizeMax) {
            cpt = 0;
        }
    }
    var result_array = arg1['split']('');
    for (cpt = 0; cpt < result_array['length']; cpt++) {
        result_array[const_array[cpt]] = arg1['charAt'](cpt);
    }
    return result_array['join']('');
}

function _0x53e54e(arg1) {
    var const_array =[0, 21, 0, 34, 4, 9, 23, 30, 14, 5, 29, 4, 24, 22, 8, 20, 31, 17, 38, 35, 15, 1, 13, 6, 12, 26, 25, 27, 33, 10, 7, 16, 32, 28, 3, 19,37, 36, 18, 39];
    var const1 = '9o#jzQ$=W8sN>n?kIXuIM7sh6 WilbDPx`1&YF5z';
    var cpt = 0;
    var sizeMax = const1['length']; //40
    while (arg1['length'] < 40) {
        arg1 += const1[cpt++];
        if (cpt >= sizeMax) {
            cpt = 0;
        }
    }
    var array_result = arg1['split']('');
    for (cpt = 0; cpt < array_result['length']; cpt++) {
        array_result[const_array[cpt]] = arg1['charAt'](cpt);
    }
    return array_result['join']('');
}

function _0x4bf1ad(arg1) {
    var const6 = 'd[cn?k+qje)/N|t.wkGr]rO+k9b=2y,}@Zyb:8pla2\'6%dn)';
    var chars = arg1['split'](''); // 0x3
    var var_temp = 0;
    for (var i = 0; i < chars['length']; i++) { // lenght
        var_temp = arg1['charCodeAt'](i) ^ const6['charCodeAt'](i) & 15;
        chars[i] = String['fromCharCode'](var_temp);
        if (var_temp < 32 || var_temp > 126) {
        }
    }
    return chars['join']('');
}
