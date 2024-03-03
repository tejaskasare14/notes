fetch("https://api.github.com/users")
.then((resp)=>
      {
         resp.json()
         .then((data)=>
            {
               console.log(data);
            })
         .catch((err)=>{console.log(err);})
      })
.catch((err)=>{console.log(err);})

console.log("Hello js");


async function get_users(){
    try
    {
      let resp= await fetch("https://api.github.com/users");
      let data = await resp.json()
      console.log(data);
    }
    catch (err)
    {
      console.log("something went wrong");
    }
}
get_users()
console.log("bye js");





