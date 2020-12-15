const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.status(200).send({message: 'Olá mundo, esto funcionando!'});
})

app.get('/ola',(req,res ) => {
    res.status(200).send({message: 'Oi, estou rodando!'})
})

app.listen(3001, ()=>{
    console.log("Api rodando na porta 3001");
})
