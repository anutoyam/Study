const { fileLoader } = require('ejs');
const express = require('express');
const snap7 = require('node-snap7');
const app = express();

//constructor
const arrWord = new Array();
let arrBool = new Array();
const wordLengh = 48;
const boolLengh = 4;

const s7client = new snap7.S7Client();

app.set('views', __dirname + '/view')
app.set('view engine', 'ejs')
app.engine('html', require('ejs').renderFile)

app.get('/', (req, res) => {
    res.render('index', {
        name: '이문환',
        arrWord: arrWord,
        arrBool: arrBool
    })
})

app.listen(3000, function () {
    console.log("port 3000");
    plcConnect();
    plcRead();
    plcDisconnect();
})

function plcConnect() {
    s7client.ConnectTo('192.168.0.95', 0, 2, function (err) {
        if (err) 
            return console.log(
                '>> Connection failed. Code #' + err + ' - ' + s7client.ErrorText(err)
            );
        }
    )
};

function plcDisconnect() {
    s7client.Disconnect();
}

function plcRead() {

    s7client.DBRead(59, 0, wordLengh, function (err, res) {
        if (err) 
            return console.log(
                '>> DBRead Failed. Code #' + err + ' - ' + s7client.ErrorText(err)
            );
        //Word Data Read
        for (let i = 0; i < wordLengh / 2; i++) {
            //Word를 Read하기에 0,1.. 번째 값을 hex -> dec 후에 bin으로 변환(tostring)후에 합침
            arrWord[i] = [res[i * 2].toString(2), res[i * 2 + 1].toString(2)];
            //8자리 빈공간에 0을 채움
            arrWord[i] = arrWord[i].map(fillZero);
            // 8비트 배열 2개를 합침(16비트)
            arrWord[i] = arrWord[i].join('');
            //bin을 dec로 변환
            arrWord[i] = parseInt(arrWord[i],2) ;
            //최상위 비트 확인 후 음수로 변경
            if ((arrWord[i] & 0x8000) > 0) {
                arrWord[i] = arrWord[i] - 0x10000;
             }
        }
        console.log(arrWord);
    });

    s7client.DBRead(59, wordLengh, boolLengh, function (err, res) {
        if (err) 
            return console.log(
                '>> DBRead Failed. Code #' + err + ' - ' + s7client.ErrorText(err)
            );
        
        //앞자리에 0 이있다면 생략하는 버그 고쳐야함
        let arrBit = Array();
        for (let i = 0; i < res.length; i++) {
            //3차 정리
            arrBool[i] = res[i].toString(2);
            arrBool[i] = fillZero(arrBool[i]);
            arrBool[i] = arrBool[i].split('').reverse();
            arrBool[i] = arrBool[i].join('');         
            
            // const bin = res[i].toString(2);
            
            // 1차 시도 실패
            // fillZero(bin);
            // arrBit.push(...bin.split("").reverse());

            // 2차 시도 성공 - 이렇게 해야 가능
            //zeroBin =fillZero(bin);
            //arrBit.push(...zeroBin.split("").reverse());
        }
        arrBool = arrBool.join('');
        arrBit= arrBool.split('')
        arrBool = arrBit.map(boolFromStringOtherwiseNull);
        console.log(arrBool);
    });
    // setTimeout( function() {     plcRead();     console.log("-----------------");
    // }, 500 );
}

//String to bool
function boolFromStringOtherwiseNull(s) {
    if (s == '1') 
        return true
    if (s == '0') 
        return false
    return null
}

//Empty Space Fill Zero
function fillZero(data){
    if (data.length !== 8){
        zero = "0";
        zeroLength = 8-data.length;
        for (let i = 0; i < zeroLength; i++) {
            data = zero + data;    
        }
    }
    return data;
}

