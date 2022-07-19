var btnStartWorker = document.getElementById('btnStartWorker'); // worker 실행 버튼
var btnStopWorker = document.getElementById('btnStopWorker'); // worker 중지 버튼
var output = document.getElementById('output'); // 받은 메시지 출력
var worker; // worker

btnStartWorker.addEventListener('click', startWorker);
btnStopWorker.addEventListener('click', stopWorker);

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