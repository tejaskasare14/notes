//getElementById()
let in_red=document.getElementById("in_red")
console.log(in_red);
in_red.style.color ="red"

let in_green=document.getElementById("in_green")
console.log(in_green);
in_green.style.color ="green"

//getElementsByTagName()
let h2 = document.getElementsByTagName("h2")
console.log(h2);
//h2.style.color="blue" ERROR

//since getElementsByTagName() is returning multiple elements, use indexing or for loop for manipulation
//h2[0].style.color="pink"
//h2[1].style.color="yellow"

for(let indivisual_h2 of h2)
{
   indivisual_h2.style.color="blue"
}

//getElementsByClassName()
let in_orange = document.getElementsByClassName("in_orange")
for(let indivisual_in_orange of in_orange)
{
   indivisual_in_orange.style.color="orange"
}

//queryselector()
let div_h1 = document.querySelector("div>h1") //get first occurance where h1 inside div
div_h1.style.color="pink"

//queryselectorall()
let div_h1_all = document.querySelectorAll("div>h1")
for (let elemenet of div_h1_all)
{
   elemenet.style.backgroundColor = "yellow"
}