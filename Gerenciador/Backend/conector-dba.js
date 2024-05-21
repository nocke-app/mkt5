const mysql = require('mysql');

// Configuração da conexão com o banco de dados
const connection = mysql.createConnection({
  host: 'localhost', // Seu host MySQL
  user: 'seu_usuario', // Seu usuário MySQL
  password: 'sua_senha', // Sua senha MySQL
  database: 'nome_do_banco' // Seu banco de dados MySQL
});

// Conectar ao banco de dados
connection.connect((err) => {
  if (err) {
    console.error('Erro ao conectar ao banco de dados:', err);
    return;
  }
  console.log('Conexão bem-sucedida ao banco de dados!');
});

// Exemplo de consulta ao banco de dados
connection.query('SELECT * FROM clientes', (err, rows) => {
  if (err) {
    console.error('Erro ao executar a consulta:', err);
    return;
  }
  console.log('Resultado da consulta:', rows);
});

// Fechar a conexão com o banco de dados quando não for mais necessário
connection.end();
