let my_h1 = document.getElementById("my_h1")
let my_btn = document.getElementById("my_btn")


my_btn.addEventListener("dblclick",()=>{
   my_h1.style.color="red"
   my_h1.textContent = "I am changed !!!"
})

//color changing logic
let box = document.getElementById("box")
let start_btn = document.getElementById("start_btn")
let stop_btn = document.getElementById("stop_btn")

let colors = ["red","green","purple","aqua","brown","yellow","pink","orange","black","blue"]
let my_interval;
start_btn.addEventListener("click",()=>{
   //box.style.backgroundColor="red"
   //console.log(Math.floor(Math.random()*10));
   //let index = Math.floor(Math.random()*10)
   //console.log(colors[index]);

   my_interval=setInterval(() => {
      let index = Math.floor(Math.random()*10)
      box.style.backgroundColor=colors[index]
   }, 300);
})
stop_btn.addEventListener("click",()=>{
   clearInterval(my_interval)
})

//understanding inner html
let parent = document.getElementById("parent")
let btn = document.getElementById("btn")

btn.addEventListener("click",()=>{
   parent.innerHTML = "<h1>Hello</h1>"
})




