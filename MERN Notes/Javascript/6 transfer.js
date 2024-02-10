// break continue
//break => based on condition, if we want to terminate the loop
//continue =>based on condition, if we want to skip current iteration

let prices = [199,99,299,199,399,99]
//dont buys item with price 99
for(let price of prices)
{
   if(price==99)
   {
      continue
   }
   else
   {
      console.log(price, "added to cart");
   }
}
//dont buy anything asa you get 99
console.log("break");
for(let price of prices)
{
   if(price==99)
   {
      break
   }
   else
   {
      console.log(price, "added to cart");
   }
}