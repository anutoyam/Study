//event
const h1 = document.querySelector("div.hello:first-child h1");


/*
function handleTitleClick() {
    const clickedClass = "clicked"
    if (h1.classList.contains(clickedClass)) {
        h1.classList.remove(clickedClass);
    } else {
        h1.classList.add(clickedClass);
    }
}
*/
//아래 코드와 같은 기능을 한다.

function handleTitleClick() {
    h1.classList.toggle("clicked");
}

h1.addEventListener("click", handleTitleClick);
