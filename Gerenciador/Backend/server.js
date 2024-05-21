const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

// Configuração do body-parser para lidar com requisições JSON
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Rota para autenticação de login
app.post('/login', (req, res) => {
    const { username, password } = req.body;

    // Aqui você pode adicionar a lógica de autenticação
    if (username === 'admin' && password === 'admin') {
        res.json({ success: true, message: 'Login successful' });
    } else {
        res.status(401).json({ success: false, message: 'Invalid username or password' });
    }
});

// Rota para obter dados do painel de administração
app.get('/dashboard', (req, res) => {
    // Aqui você pode adicionar a lógica para fornecer os dados do painel de administração
    // Por enquanto, vamos apenas retornar uma mensagem de sucesso
    res.json({ success: true, message: 'Dashboard data retrieved successfully' });
});

// Rota para fazer logout
app.post('/logout', (req, res) => {
    // Aqui você pode adicionar a lógica de logout
    // Por enquanto, vamos apenas retornar uma mensagem de sucesso
    res.json({ success: true, message: 'Logout successful' });
});

// Inicialização do servidor
app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`);
});
