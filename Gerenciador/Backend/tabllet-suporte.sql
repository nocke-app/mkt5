CREATE TABLE Suporte (
    id INT AUTO_INCREMENT PRIMARY KEY,
    assunto VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL,
    status ENUM('Não Resolvido', 'Resolvido') NOT NULL,
    data_solicitacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);






/* Informações sobre o sql suporte  
id: Identificador único para cada solicitação de suporte.
assunto: O assunto da solicitação de suporte.
descricao: Uma descrição detalhada da solicitação de suporte.
status: O status da solicitação de suporte, que pode ser "Não Resolvido" ou "Resolvido".
data_solicitacao: A data e hora em que a solicitação de suporte foi criada. Este campo é preenchido automaticamente com a data e hora atuais quando uma nova solicitação é adicionada.