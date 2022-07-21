const express = require('express');
const snap7 = require('node-snap7');

const app = express();
//word byte
const arrWord = new Array(24);
const s7client = new snap7.S7Client();

app.set('views', __dirname + '/view')
app.set('view engine', 'ejs')
app.engine('html', require('ejs').renderFile)

app.get('/', (req, res) => {
    res.render('index', {
        name: '이문환',
        array: arrWord
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

    s7client.DBRead(59, 0, 48, function (err, res) {
        if (err) 
            return console.log(
                '>> DBRead Failed. Code #' + err + ' - ' + s7client.ErrorText(err)
            );
        
        for (let i = 0; i < res.length / 2; i++) {
            length = res.length / 2
            arrWord[i] = res[i * 2 + 1];
        }
        console.log(res);
    });
    

    s7client.DBRead(59, 48, 1, function (err, res) {
        if (err) 
            return console.log(
                '>> DBRead Failed. Code #' + err + ' - ' + s7client.ErrorText(err)
            );

            console.log(res[0]);

    });

    // setTimeout( function() {
    //     plcRead();
    //     console.log("-----------------");
    // }, 500 );
    
}