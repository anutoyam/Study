const toDoForm = document.getElementById("todo-form");
const toDoInput = toDoForm.querySelector("input");
const toDoList = document.getElementById("todo-list");
const arrTodo = [];
const TODO = "todo";


function deleteTodo(event) {    
    //내가 짠 코드 - 역순으로 지워도 순서대로 지워지는 오류가 있음.
    //event.preventDefault();
    //const li = toDoList.querySelector("li");
    //console.dir(event.target.parentElement);
    //toDoList.removeChild(li);

    //강의 코드
    const li = event.target.parentElement;
    li.remove();
    
    //내가 짠 local stroage 삭제 기능
    const removeItem = arrTodo.indexOf(event.target.parentElement.firstChild.innerText);
    delete arrTodo[removeItem];
    const delTodo = arrTodo.filter(arrTodo => arrTodo !== "empty");
    
    localStorage.setItem("todo",JSON.stringify(delTodo));
    
}

function saveLocalStorage(saveTodo){
    arrTodo.push(saveTodo);
    localStorage.setItem("todo",JSON.stringify(arrTodo));
    
}

function paintTodo(newTodo) {
    const li = document.createElement("li");
    const span = document.createElement("span");
    span.innerText = newTodo;
    const button = document.createElement("button");
    button.innerText = "❌";
    button.addEventListener("click", deleteTodo);
    li.appendChild(span);
    li.appendChild(button);
    toDoList.appendChild(li);
}

function handleToDoSubmit(event) {
    event.preventDefault();
    const newTodo = toDoInput.value;
    toDoInput.value = "";
    saveLocalStorage(newTodo);
    paintTodo(newTodo);
}

const output = localStorage.getItem(TODO);
const savedTodo = JSON.parse(output);
if(output !== null){
    for(i=0; i<savedTodo.length; i++){
        arrTodo.push(savedTodo[i]);
        paintTodo(savedTodo[i]);
    }
}

toDoForm.addEventListener("submit", handleToDoSubmit);

