const express = require('express');
const snap7 = require('node-snap7');
const app = express();

//constructor
let arrWord = new Array();
let arrBool = null;
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
        
        //생략된 0 채우는 중
        for (let i = 0; i < res.length / 2; i++) {
            //length = res.length / 2 arrWord[i] = res[i * 2 + 1];
            arrWord[i] = [].concat(res[i * 2].toString(2), res[i * 2 + 1].toString(2));
            arrWord[i] = arrWord[i].map(fillZero);
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
            const bin = res[i].toString(2);

            arrBit.push(...bin.split("").reverse());
        }
        arrBool = arrBit.map(boolFromStringOtherwiseNull);

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

