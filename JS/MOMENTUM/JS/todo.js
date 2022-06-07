const toDoForm = document.getElementById("todo-form");
const toDoInput = toDoForm.querySelector("input");
const toDoList = document.getElementById("todo-list");

const TODOS_KEY = "todos";

let toDos = [];

function saveToDos() {
    localStorage.setItem("todos", JSON.stringify(toDos));
}

function deleteTodo(event) {
    // 내가 짠 코드 역순으로 지워도 순서대로 지워지는 오류가 있음. 
    // event.preventDefault(); 
    // const li = toDoList.querySelector("li"); 
    //console.dir(event.target.parentElement);
    
    //toDoList.removeChild(li); //강의 코드
    const li = event.target.parentElement;
    li.remove();
    toDos = toDos.filter(toDo => toDo.id !== parseInt(li.id));
    saveToDos();
}

function paintTodo(newTodo) {
    const li = document.createElement("li");
    li.id = newTodo.id;
    const span = document.createElement("span");
    span.innerText = newTodo.text;
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
    //중복값을 분류하기 위해 데이터마다 ID를 부여한다.
    const newTodoObj = {
        text:newTodo,
        id:Date.now(),
    };
    toDos.push(newTodoObj);
    paintTodo(newTodoObj);
    saveToDos();
}

toDoForm.addEventListener("submit", handleToDoSubmit);

// solution 1) function으로 구현하기
// function sayHello(item) {
//     console.log("this is the turn of",item);
// }

const savedToDos = localStorage.getItem(TODOS_KEY);
if (savedToDos !== null){
    const parsedToDos = JSON.parse(savedToDos);
    //console.log(parsedToDos);
    // parsedToDos.forEach(sayHello);
    toDos = parsedToDos;
    //solution 2) foreach로 구현하기
    parsedToDos.forEach(paintTodo);

    //내가 짠 코드
    // for(i=0; i<parsedToDos.length; i++){
    //     paintTodo(parsedToDos[i].text);
    // }
}

function sexyFilter(){

}