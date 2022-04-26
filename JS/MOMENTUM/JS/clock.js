const clock = document.querySelector("h2#clock");

function getClock(){
    const hour = new Date().getHours();
    const min = new Date().getMinutes();
    const sec = new Date().getSeconds();

    const date = new Date();
    clock.innerText =`${hour}시 ${min}분 ${sec}초`;
    console.log(`${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`);
    
}

getClock();
setInterval(getClock, 1000);
