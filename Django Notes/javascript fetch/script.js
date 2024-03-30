let names=document.getElementById("names")

      fetch('http://localhost:8000/api/employees/')
      .then(resp => resp.json()
                        .then((data)=> 
                           {
                              let employees = data
                              //console.log(employees)
                              //console.log(employees[0].name)
                              for(emp of employees)
                              {
                                 //console.log(emp.name)
                                 names.innerHTML += `<h1>${emp.name}</h1>`
                              }
                              
                           })
                        .catch())
      .catch()

// h