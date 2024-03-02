//every loop must follow 3 rules
//1. initialization
//2. condition to terminate
//3. inc/dec
//for loop syntax
//for(initialization;condition;inc/dec)

//print 1-5 numbers using for loop
for(let i=1; i<=5; i++)
   {
      console.log(i);
   }

// 1 4 27 256 3125
for(let i=1; i<=5; i++)
   {
      console.log(i**i);
   }

// for loop on array
console.log("-- for loop on array type 1 --");
prices = [199,99,49,199,299,49]
for(let i=0; i<prices.length; i++)
   {
      console.log(prices[i]);
   }

console.log("-- for loop on array type 2 --");
for (price of prices)
   {
      console.log(price);
   }

console.log("-- for loop on array type 3 --");
for (price in prices)
   {
         console.log(price,prices[price]);
   }


