//event
const h1 = document.querySelector("div.hello:first-child h1");

function handleTitleClick() {
    h1.style.color = "blue";
}

function handleMouseEnter(){
    h1.innerText = "Mouse is here";
}

function handleMouseLeave(){
    h1.innerText = "Mouse is gone!";
}

function handleWindowReisize(){
    document.body.style.backgroundColor = "tomato";
}

function handleWindowCopy(){
    alert("Copier!");
}

function handleWifiOnline(){
    alert("Wifi Online");
}

function handleWifiOffline(){
    alert("Wifi Offline");
}

//이렇게도 가능
h1.onclick = handleTitleClick; 

//title.addEventListener("click", handleTitleClick);
h1.addEventListener("mouseenter", handleMouseEnter);
h1.addEventListener("mouseleave", handleMouseLeave);

window.addEventListener("resize", handleWindowReisize);
window.addEventListener("copy", handleWindowCopy);
window.addEventListener("offline", handleWifiOffline);
window.addEventListener("online", handleWifiOnline);

console.dir(h1);

