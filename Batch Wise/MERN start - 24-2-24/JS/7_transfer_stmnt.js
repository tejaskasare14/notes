
prices=[199,299,99,399,499,99,899]
console.log("----continue-----");
for (price of prices)
   {
      if(price==99)
      {
         continue; //go for next interatation
         //control goes towrods the loop line 3
      }
      console.log(`${price} added to cart`);
   }

console.log("-----break----");
for (price of prices)
   {
      if(price==99)
      {
         break; //go out of the loop. terminate the loop
         //control goes out of the loop line 24
      }
      console.log(`${price} added to cart`);
   }
