const todoForm = document.getElementById("todo-form");
const todoList = document.getElementById("todo-list");
const submitBtn = document.querySelector(".submitBtn");

function submitAddTodo(event){
	event.preventDefault(); //새로고침방지
    const todo = content.value;
    window.localStorage.setItem("todo", todo);
    content.value = "";
    paintTodo(todo);
};

todoForm.addEventListener("submit", submitAddTodo);

function paintTodo() {
    
}