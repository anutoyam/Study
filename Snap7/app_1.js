const {fileLoader} = require('ejs');
const express = require('express');
const plc = require("./plcCon.js")
const DO = require("./dataobject.js");
const fs = require("fs");

const app = express();

let data = new Array();
let count = 0;
let OnOff = true;

//CSS Load
app.use(express.static(__dirname));

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

async function ReadPlc() {
    try {
        data = await DO.ProccessData();
        const time = newTime();
        fs.writeFileSync(
            "./plcData/" + time[0] + "txt",
            "[" + time[1] + "]" + data + '\n',
            {flag: 'a+'}
        );
        setTimeout(function () {
            if (OnOff = true) {
                console.log("--------" + count + "---------");
                ReadPlc();
                count++
            }else{
                return;
            }
        }, 1000);
    } catch  {
        return;
    }

}

const newTime = function () {
    const today = new Date();
    const date = today.toLocaleDateString();
    const time = today.toLocaleString('en-US');
    return [date, time];
}

process.once('SIGINT', () => {
    OnOff = false;
    plc.plcDisconnect();
    console.log("You've pressed Ctrl + C on this process.");
})