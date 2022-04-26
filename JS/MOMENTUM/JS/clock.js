const clock = document.querySelector("h2#clock");

function getClock() {
    const date = new Date();
    const hour = String(new Date().getHours()).padStart(2, "0");
    const min = String(new Date().getMinutes()).padStart(2, "0");
    const sec = String(new Date().getSeconds()).padStart(2, "0");

    clock.innerText = `${hour}시 ${min}분 ${sec}초`;
    //console.log(`${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`);
}

getClock();
setInterval(getClock, 1000);
