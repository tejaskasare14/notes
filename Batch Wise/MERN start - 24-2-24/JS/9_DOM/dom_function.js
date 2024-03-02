//getElementById()
let in_green=document.getElementById("in_green")
let in_red=document.getElementById("in_red")
console.log(in_green);
in_green.style.color = "green";
in_red.style.color="red"

//getElementsByTagName()
let h2 = document.getElementsByTagName("h2")
console.log(h2);
//h2.style.color = "blue";
for (indivisual_h2 of h2)
{
   indivisual_h2.style.color = "blue";
}

//getElementsByClassName()
let in_purple = document.getElementsByClassName("in_purple")
for (each_purple of in_purple)
{
   each_purple.style.color = "purple"
}

//queryselector()
let div_p=document.querySelector("div>p")
div_p.style.color="pink"


//querySelectorAll
let divs_ps=document.querySelectorAll("div>p")
for (divp of divs_ps)
{
   divp.style.backgroundColor="yellow"
}