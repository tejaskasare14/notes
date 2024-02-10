console.log("------continue---------");

prices=[199,299,99,399,199,99,299,399]
console.log(prices.length);
for(let i=0;i<prices.length;i++)
   {
      if(prices[i]==99) //199==99 //299==99 //99==99
      {
         continue //towards the loop
      }
      else
      {
         console.log(prices[i]);
      }
   }

console.log("------break---------");

   for(let i=0;i<prices.length;i++)
   {
      if(prices[i]==99) //199==99 //299==99 //99==99
      {
         break; //out of the loop
      }
      else
      {
         console.log(prices[i]);
      }
   }

console.log("hello js");
