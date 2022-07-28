const snap7 = require('node-snap7');
const s7client = new snap7.S7Client();

//Dataobject로 전달할 배열(DB의 전체 길이를 할당한다.)
let buffer = new Array(52);

module.exports = {
    plcConnect: function () {
        s7client.ConnectTo('192.168.0.95', 0, 2, function (err) {
            if (err) 
                return console.log(
                    '>> Connection failed. Code #' + err + ' - ' + s7client.ErrorText(err)
                );
            }
        )
    },

    plcRead: function () {
        return new Promise(function (reslove, reject) {
            s7client.DBRead(59, 0, 52, function (err, res) {
                if(err)
                    return reject(">> DBRead Failed");
                for(let i = 0; i < res.length; i++){
                    buffer[i] = res[i];
                }             
                reslove(buffer);
            })
        })
    },

    plcDisconnect: function () {
        s7client.Disconnect();
        console.log(">> Disconnect");
    }

};