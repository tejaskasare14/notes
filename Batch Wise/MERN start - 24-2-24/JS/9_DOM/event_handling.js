let my_h1 = document.getElementById("my_h1")
let my_btn = document.getElementById("my_btn")

my_btn.addEventListener("click",()=>{
   my_h1.style.color="red"
})

let my_h2 = document.getElementById("my_h2")
let my_btn2 = document.getElementById("my_btn2")

my_btn2.addEventListener("dblclick",()=>{
   my_h2.textContent = "New Text data"
})

let parent = document.getElementById("parent")
let my_btn3 = document.getElementById("my_btn3")

my_btn3.addEventListener("click",()=>{
   parent.innerHTML="<h1>Hello I am new here</h1>"
})