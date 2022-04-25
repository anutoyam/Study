//const loginForm = document.getElementById("Login-Form");
//const loginInput = loginForm.querySelector("input");
//const loginButton = loginForm.querySelector("button");

//위 아래 같음
//const loginInput = document.querySelector("#login-form input");
//const loginButton = document.querySelector("#login-form button");

const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-form input");
const link = document.querySelector("a");

function handleBtnClick(event){
    //preventDefault - 브라우저의 기본기능을 막음 : submit의 자동 새로고침을 막음
    event.preventDefault();
    const username = loginInput.value;
    if(username ===""){
        alert("Please write your name");
    }else if(username.length > 15){
        alert("Your name is too long.")
    }else{
        console.log("hello", username);
    }

}

function handleLinkClick(event){
    event.preventDefault();
    console.dir(event);
}

//loginButton.addEventListener("click",handleBtnClick)
loginForm.addEventListener("submit", handleBtnClick);
link.addEventListener("click", handleLinkClick);
//handleLinkClick()를 하게 되면 한번만 실행한다.