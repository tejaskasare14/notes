let mybtn = document.getElementById("mybtn")
let root = document.getElementById("root")

mybtn.addEventListener("click",()=>
{

   let myh1 = document.createElement("h1")
   myh1.textContent = 'hello world'
   root.appendChild(myh1)
   
})


//creating elemet directly without button click
let myp = document.createElement("p")
myp.textContent = 'this is paragraph'
root.appendChild(myp)

