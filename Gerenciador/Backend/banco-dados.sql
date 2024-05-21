-- Tabela de taxas
CREATE TABLE taxas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    tipo VARCHAR(100) NOT NULL,
    valor DECIMAL(10, 2) NOT NULL,
    descricao TEXT
);

-- Tabela de clientes
CREATE TABLE clientes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    endereco TEXT
);

-- Tabela de transações financeiras
CREATE TABLE transacoes_financeiras (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cliente_id INT,
    valor DECIMAL(10, 2) NOT NULL,
    tipo ENUM('entrada', 'saída') NOT NULL,
    descricao TEXT,
    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

-- Tabela de relatórios
CREATE TABLE relatorios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(255) NOT NULL,
    descricao TEXT,
    data DATE
);

-- Tabela de acessos
CREATE TABLE acessos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT,
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- Tabela de usuários
CREATE TABLE usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    papel ENUM('admin', 'usuario') NOT NULL
);
