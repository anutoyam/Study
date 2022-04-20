//
const h1 = document.querySelector("div.hello:first-child h1");

function handleTitleClick(){
    h1.style.color = "blue";
    console.log("title was clicked!");

}
h1.addEventListener("click",handleTitleClick);

