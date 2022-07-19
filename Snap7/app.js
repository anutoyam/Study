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

window.onload = function(){

}

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

// worker 실행
function startWorker() {

    // Worker 지원 유무 확인
    if (!!window.Worker) {

        // 실행하고 있는 워커 있으면 중지시키기
        if (worker) {
            stopWorker();
        }

        worker = new Worker('worker.js');
        worker.postMessage('워커 실행'); // 워커에 메시지를 보낸다.

        // 메시지는 JSON구조로 직렬화 할 수 있는 값이면 사용할 수 있다. Object등 worker.postMessage( { name :
        // '302chanwoo' } ); 워커로 부터 메시지를 수신한다.
        worker.onmessage = function (e) {
            console.log('호출 페이지 - ', e.data);
            output.innerHTML += e.data;
        };
    }

}
// worker 중지
function stopWorker() {

    if (worker) {
        worker.terminate();
        worker = null;
    }

}