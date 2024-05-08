from flask import Flask, jsonify, request

app = Flask(__name__)

# Exemplo de dados de usuários
usuarios = [
    {"id": 1, "nome": "Usuário 1", "email": "usuario1@example.com"},
    {"id": 2, "nome": "Usuário 2", "email": "usuario2@example.com"}
]

# Exemplo de dados de taxas
taxas = [
    {"id": 1, "nome": "Taxa Padrão", "valor": 10.00},
    {"id": 2, "nome": "Taxa Especial", "valor": 15.00}
]

# Exemplo de dados de transações em dólares
transacoes_dolares = [
    {"id": 1, "descricao": "Compra de Produto", "valor": 50.00},
    {"id": 2, "descricao": "Venda de Serviço", "valor": 100.00}
]

# Exemplo de dados de faturas
faturas = [
    {"id": 1, "numero": "001", "valor": 100.00},
    {"id": 2, "numero": "002", "valor": 150.00}
]

# Rotas para gerenciamento de usuários
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    return jsonify(usuarios)

@app.route('/usuarios', methods=['POST'])
def add_usuario():
    data = request.json
    new_usuario = {
        "id": len(usuarios) + 1,
        "nome": data['nome'],
        "email": data['email']
    }
    usuarios.append(new_usuario)
    return jsonify({"message": "Usuário adicionado com sucesso!"}), 201

@app.route('/usuarios/<int:usuario_id>', methods=['PUT'])
def update_usuario(usuario_id):
    data = request.json
    for usuario in usuarios:
        if usuario['id'] == usuario_id:
            usuario['nome'] = data['nome']
            usuario['email'] = data['email']
            return jsonify({"message": "Usuário atualizado com sucesso!"}), 200
    return jsonify({"error": "Usuário não encontrado"}), 404

@app.route('/usuarios/<int:usuario_id>', methods=['DELETE'])
def delete_usuario(usuario_id):
    for usuario in usuarios:
        if usuario['id'] == usuario_id:
            usuarios.remove(usuario)
            return jsonify({"message": "Usuário excluído com sucesso!"}), 200
    return jsonify({"error": "Usuário não encontrado"}), 404

# Rotas para gerenciamento de taxas
@app.route('/taxas', methods=['GET'])
def get_taxas():
    return jsonify(taxas)

@app.route('/taxas', methods=['POST'])
def add_taxa():
    data = request.json
    new_taxa = {
        "id": len(taxas) + 1,
        "nome": data['nome'],
        "valor": data['valor']
    }
    taxas.append(new_taxa)
    return jsonify({"message": "Taxa adicionada com sucesso!"}), 201

@app.route('/taxas/<int:taxa_id>', methods=['PUT'])
def update_taxa(taxa_id):
    data = request.json
    for taxa in taxas:
        if taxa['id'] == taxa_id:
            taxa['nome'] = data['nome']
            taxa['valor'] = data['valor']
            return jsonify({"message": "Taxa atualizada com sucesso!"}), 200
    return jsonify({"error": "Taxa não encontrada"}), 404

@app.route('/taxas/<int:taxa_id>', methods=['DELETE'])
def delete_taxa(taxa_id):
    for taxa in taxas:
        if taxa['id'] == taxa_id:
            taxas.remove(taxa)
            return jsonify({"message": "Taxa excluída com sucesso!"}), 200
    return jsonify({"error": "Taxa não encontrada"}), 404

# Rotas para gerenciamento de transações em dólares
@app.route('/transacoes', methods=['GET'])
def get_transacoes():
    return jsonify(transacoes_dolares)

@app.route('/transacoes', methods=['POST'])
def add_transacao():
    data = request.json
    new_transacao = {
        "id": len(transacoes_dolares) + 1,
        "descricao": data['descricao'],
        "valor": data['valor']
    }
    transacoes_dolares.append(new_transacao)
    return jsonify({"message": "Transação em dólares adicionada com sucesso!"}), 201

# Rotas para gerenciamento de faturas
@app.route('/faturas', methods=['GET'])
def get_faturas():
    return jsonify(faturas)

@app.route('/faturas', methods=['POST'])
def add_fatura():
    data = request.json
    new_fatura = {
        "id": len(faturas) + 1,
        "numero": data['numero'],
        "valor": data['valor']
    }
    faturas.append(new_fatura)
    return jsonify({"message": "Fatura adicionada com sucesso!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
