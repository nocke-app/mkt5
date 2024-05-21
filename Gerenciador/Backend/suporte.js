const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

// Middleware para analisar corpos de solicitação JSON
app.use(bodyParser.json());

// Rota para lidar com o recebimento de solicitações de suporte
app.post('/solicitacoes', (req, res) => {
    const solicitacao = req.body; // Assume que o corpo da solicitação contém os dados da solicitação

    // Lógica para processar a solicitação e salvar no banco de dados ou em outro local
    console.log('Solicitação de suporte recebida:', solicitacao);
    
    // Responde ao cliente com uma mensagem de sucesso
    res.status(200).send('Solicitação de suporte recebida com sucesso.');
});

// Inicia o servidor
app.listen(port, () => {
    console.log(`Servidor de suporte está ouvindo em http://localhost:${port}`);
});
