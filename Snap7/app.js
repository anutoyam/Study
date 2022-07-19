const express = require('express');
const app = express();
const ejs = require('ejs');
const snap7 = require('node-snap7');
var arr = new Array(4);

app.set('views', __dirname + '/view')
app.set('view engine', 'ejs')
app.engine('html', require('ejs').renderFile)

app.get('/', (req, res) => {
    res.render('index', {
        name: '홍길동',
        array: arr
    })
})

const server = app.listen(3000, function () {
    console.log("port 3000");
    plcRead();
})

function plcRead() {
    var s7client = new snap7.S7Client();
    s7client.ConnectTo('192.168.0.95', 0, 2, function (err) {

        if (err) 
            return console.log(
                '>> Connection failed. Code #' + err + ' - ' + s7client.ErrorText(err)
            );
        
        s7client.DBRead(59, 2, 8, function (err, res) {
            if (err) 
                return console.log(
                    '>> DBRead Failed. Code #' + err + ' - ' + s7client.ErrorText(err)
                );
            
            for (let i = 0; i < res.length / 2; i++) {
                length = res.length / 2
                arr[i] = res[i * 2 + 1];
            }
        });
    });
    s7client.Disconnect();
}