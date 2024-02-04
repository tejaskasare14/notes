const express = require('express')
const router = express.Router()
router.use(express.json())

let users = [
   {
      id:1,
      name:"raj",
      age:25
   },
   {
      id:2,
      name:"rani",
      age:35
   }
]

router.get('/users', (req, res) => {
   // res.send(users)
   if(users.length!=0)
   {
      return res.status(200).send(
         {
            message:"following user found",
            data:users
         }
      )
   }
   else
   {
      return res.status(404).send(
         {
            message:`There are no users, please add some`,
            data:[]
         }
      )
   }  
})

router.get('/users/search',(req,res)=>{
   const {name}=req.query
   const fetchedUsers=users.filter(user=>user.name.toLowerCase().includes(name.toLocaleLowerCase()))
   if(fetchedUsers.length!=0)
   {
      return res.status(200).send(
         {
            message:"following user found",
            data:fetchedUsers
         }
      )
   }
   else
   {
      return res.status(404).send(
         {
            message:`There are no users, with name ${name}`,
            data:null
         }
      )
   }  
   
})

router.get('/users/:id', (req, res) => {
   const user_id = req.params.id
   const user=users.filter(user=>user.id === +user_id) //+user_id means, converted to number
   if(user.length!=0)
   {
      return res.status(200).send(
         {
            message:"following user found",
            data:user
         }
      )
   }
   else
   {
      return res.status(404).send(
         {
            message:`user with id ${user_id} does not exist`,
            data:null
         }
      )
   }
   
})

router.post('/users',(req,res)=>{
   const {name,age}=req.body
   const user = 
   {
      id:users.length+1,
      name,
      age
   }

   users.push(user)

   res.status(200).send(
      {
         message:`user added successfully`,
         data:user
      }
   )
})

router.put('/users/:id',(req,res)=>{
   const id=req.params.id
   const user = users.find(u=>u.id=== +id)
   if(user)
   {
      const {name,age}=req.body
      user.name = name
      user.age = age
      res.status(200).send(
         {
            message:`user with id ${id} updated with follwing details`,
            data:user
         })
   }
   else
   {
      res.status(404).send(
         {
            message:`user with id ${id} doest not exists`,
            data:null
         })
   }
})

router.patch('/users/:id',(req,res)=>{
   const id=req.params.id
   const user = users.find(u=>u.id=== +id)
   if(user)
   {
      const {name,age}=req.body
      if(name) {user.name = name}
      if(age) {user.age = age}
      res.status(200).send(
         {
            message:`user with id ${id} updated with follwing details`,
            data:user
         })
   }
   else
   {
      res.status(404).send(
         {
            message:`user with id ${id} doest not exists`,
            data:null
         })
   }
})

router.delete('/users/:id',(req,res)=>{
   const id=req.params.id
   const user = users.find(u=>u.id=== +id)
   if(user)
   {
      users = users.filter(u => u.id !== +id)
      res.status(200).send(
         {
            message:`user with id ${id} deleted`,
            data:null
         })
   }
   else
   {
      res.status(404).send(
         {
            message:`user with id ${id} doest not exists`,
            data:null
         })
   }
})

module.exports = router