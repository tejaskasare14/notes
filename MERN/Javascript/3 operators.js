//arithmatic => +,-,*,/,%,**,++,--
//assignment => =,+=,-=....
//comarision => >,<,>=,<=,!=,==,===
//logical    => &&,||,!
//bitwise    => &,|,~,^,<<,>>
//ternary    => ?

//Arithmatic
console.log("---- Arithmatic ----");
console.log(10/2);
console.log(10.0/2);
console.log(10/3);
console.log(10/0);
console.log(10**2);
let a = 10
console.log(++a);
console.log(a);
let b=20
console.log(b++);
console.log(b);

let c = 30
console.log(--c);
console.log(c);

let d=40
console.log(d--);
console.log(d);

//Assignmentr
console.log("---- Assigmnetn ----");
let e = 50
e = e+1 //e+=1
console.log(e);
e-=1 //e = e-1 
console.log(e);

//comparison
console.log("---- comparison ----");
console.log(10 > 5);
console.log(10 < 5);
console.log(10 >= 10);
console.log(10 <= 10);
console.log(10 == 10.0); //only content comarision no datatype
console.log(10 == "10"); //only content comarision no datatype
console.log(10 === "10"); //content comarision with datatype
console.log(10 === 10.0);

//logical
// && => both conditions must be true => true
// || => at least one condition must be true => true
// ! => reverse the result
console.log("---- logical ----");
console.log(10>5 && 10>2);
console.log(10<5 && 10>2);
console.log(10>5 && 10<2);

console.log(10>5 || 10>2);
console.log(10>5 || 10<2);
console.log(10<5 || 10>2);

// and => false
// or => true

console.log(! 10>2);

//ternary
console.log("---- ternary ----");
// condition ? value if true : value if false
console.log(10>2 ? "yes":"no");
console.log(10<2 ? "yes":"no");


//bitwise
console.log("---- bitwise ---");
// & => set bit to 1 if both bits are 1
// | => set bit to 1 if at least one bit is 1
// ^ => set bit to 1 if both bits are different
// ~ => reverse the bit
// << => shift bits to the left by given number
// >> => shift bits to the right by given number

// 6 => 0 0 0 0 0 1 1 0
// 9 => 0 0 0 0 1 0 0 1
//-----------------------
// & => 0 0 0 0 0 0 0 0  => 0 in decimal
//-----------------------
// | => 0 0 0 0 1 1 1 1  => 15 in decimal
//-----------------------
// ^ => 0 0 0 0 1 1 1 1  => 15 in decimal
console.log(6&9);
console.log(6|9);
console.log(6^9);

// 6 => 0 0 0 0 0 1 1 0
//~6 => 1 1 1 1 1 0 0 1   //here MSB is 1 so, the number is negative

// we cant represent -ve number directly into memory, we have
// to take 2s complement

// 6 => 0 0 0 0 0 1 1 0
//~6 => 1 1 1 1 1 0 0 1
//1s => 0 0 0 0 0 1 1 0
//2s                + 1
//-------------------------
//      0 0 0 0 0 1 1 1  ==> result is 7
// since MSB was 1 so the result must be negative 
// therefore final result is -7
console.log(~6);

console.log(6>>2);
console.log(6<<3);
