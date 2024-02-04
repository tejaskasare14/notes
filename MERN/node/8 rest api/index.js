const express = require('express')
const app = express()
require('dotenv').config()
const PORT = process.env.PORT

const userRoutes = require('./routes/user.routes')

app.get('/', (req, res) => {
   res.send("Hello World")
})

app.use('/api',userRoutes)

app.get('**', (req, res) => {
   res.status(404).send("Resource not found")
})

app.listen(PORT, () => { 
   console.log(`server is running on http://localhost:${PORT}`); 
})