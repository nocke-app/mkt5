
# Documentação de Instalação e Execução da Aplicação

Este guia fornecerá instruções detalhadas sobre como instalar e executar a aplicação que desenvolvemos, incluindo o frontend administrativo, o backend Node.js e a conexão com o banco de dados MySQL.

## Requisitos Prévios

Antes de começar, certifique-se de ter os seguintes requisitos instalados em sua máquina:

1. **Node.js e npm**: O ambiente Node.js é necessário para executar o backend e instalar as dependências do projeto. Você pode baixar e instalar o Node.js a partir do [site oficial](https://nodejs.org/).

2. **MySQL Server**: Você precisa ter o servidor MySQL instalado em sua máquina. Você pode baixar e instalar o MySQL Server a partir do [site oficial do MySQL](https://dev.mysql.com/downloads/mysql/).


## Passo 2: Configurando o Banco de Dados

1. Abra o terminal ou prompt de comando e acesse o diretório da aplicação clonada.

2. Abra o arquivo `database.sql` no diretório da aplicação. Este arquivo contém o esquema do banco de dados MySQL necessário para a aplicação.

3. Execute os comandos SQL contidos no arquivo `database.sql` no seu cliente MySQL de preferência para criar o banco de dados e as tabelas necessárias.

## Passo 3: Configurando o Backend Node.js

1. Abra o terminal ou prompt de comando e navegue até o diretório `backend` da aplicação.

2. Instale as dependências do backend executando o seguinte comando:

```
npm install
```

## Passo 4: Conectando o Backend ao Banco de Dados

1. No diretório `backend`, abra o arquivo `config.js` em um editor de texto.

2. Edite as configurações de conexão com o banco de dados (`host`, `user`, `password` e `database`) de acordo com as configurações do seu ambiente MySQL.

## Passo 5: Iniciando o Backend Node.js

No diretório `backend`, execute o seguinte comando para iniciar o servidor Node.js:

```
node server.js
```

Isso iniciará o backend Node.js e estará pronto para aceitar solicitações HTTP.

## Passo 6: Configurando o Frontend

1. Abra o terminal ou prompt de comando e navegue até o diretório raiz da aplicação.

2. No diretório raiz, abra o arquivo `index.html` em um navegador da web. Isso abrirá a interface administrativa da aplicação.

## Passo 7: Explorando a Aplicação

Agora você pode explorar a aplicação administrativa, visualizar os diferentes módulos (taxas, clientes, financeiro, relatórios, acessos), adicionar/editar/remover dados conforme necessário e interagir com o backend Node.js.

## Passo 8: Encerrando a Aplicação

Quando terminar de usar a aplicação, você pode encerrar o servidor Node.js pressionando `Ctrl + C` no terminal ou prompt de comando em que o servidor está sendo executado.

