let myDiv = document.getElementById("myDiv")

fetch("https://api.github.com/users")
.then(data => data.json()
                     .then(converted_data => 
                        {
                           console.log(converted_data)
                           for (user of converted_data)
                           {
                              console.log(user.login);
                              myDiv.innerHTML += `<h3>Name : ${user.login}</h3>`
                           }
                        })
                     .catch())
.catch(error => {console.log(error);})