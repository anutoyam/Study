const {fileLoader} = require('ejs');
const express = require('express');
const app = express();

const plc = require("./plcCon.js")
const DO = require("./dataobject.js");
const fs = require("fs");

let data = new Array();
let count = 0;


app.set('views', __dirname + '/view')
app.set('view engine', 'ejs')
app.engine('html', require('ejs').renderFile)

app.get('/', (req, res) => {
    res.render('index', {
        name: 'TEST',
        data1: data[0],
        data2: data[1]
    })
})

app.listen(3000, function () {
    console.log("port 3000");

})

plc.plcConnect();
ReadPlc();

//plc.plcDisconnect();

async function ReadPlc(){ 
    data = await DO.ProccessData();
    const time = newTime();
    fs.writeFileSync("./plcData/"+time[0]+"txt", "["+ time[1]+"]" + data + '\n', {flag: 'a+'});

    setTimeout(function () {
        ReadPlc();
        console.log("--------" + count +"---------");
        count++
    }, 1000);
}

const newTime = function(){
    const today = new Date();
    const date = today.toLocaleDateString();
    const time = today.toLocaleString('en-US');
    return [date,time];
}