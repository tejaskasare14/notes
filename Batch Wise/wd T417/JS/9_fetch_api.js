fetch("https://api.github.com/users")
.then((data)=>
            {
               data.json()
               .then(users => 
                  {
                     //console.log(users[0].login)
                     for(let i=0;i<users.length;i++)
                     {
                        console.log(users[i].login)
                     }
                  })
               .catch()

            })
.catch((err)=>{console.log(err);})