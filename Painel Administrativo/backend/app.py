from flask import Flask, jsonify, request

app = Flask(__name__)

# Exemplo de dados de usuários
usuarios = [
    {"id": 1, "nome": "Usuário 1", "email": "usuario1@example.com"},
    {"id": 2, "nome": "Usuário 2", "email": "usuario2@example.com"}
]

# Rota para obter todos os usuários
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    return jsonify(usuarios)

# Rota para adicionar um novo usuário
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

# Rota para atualizar um usuário existente
@app.route('/usuarios/<int:usuario_id>', methods=['PUT'])
def update_usuario(usuario_id):
    data = request.json
    for usuario in usuarios:
        if usuario['id'] == usuario_id:
            usuario['nome'] = data['nome']
            usuario['email'] = data['email']
            return jsonify({"message": "Usuário atualizado com sucesso!"}), 200
    return jsonify({"error": "Usuário não encontrado"}), 404

# Rota para excluir um usuário existente
@app.route('/usuarios/<int:usuario_id>', methods=['DELETE'])
def delete_usuario(usuario_id):
    for usuario in usuarios:
        if usuario['id'] == usuario_id:
            usuarios.remove(usuario)
            return jsonify({"message": "Usuário excluído com sucesso!"}), 200
    return jsonify({"error": "Usuário não encontrado"}), 404

# Exemplo de dados de taxas
taxas = [
    {"id": 1, "nome": "Taxa Padrão", "valor": 10.00},
    {"id": 2, "nome": "Taxa Especial", "valor": 15.00}
]

# Rotas para gerenciamento de taxas
@app.route('/taxas', methods=['GET'])
def get_taxas():
    return jsonify(taxas)

# Rota para adicionar uma nova taxa
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

# Rota para atualizar uma taxa existente
@app.route('/taxas/<int:taxa_id>', methods=['PUT'])
def update_taxa(taxa_id):
    data = request.json
    for taxa in taxas:
        if taxa['id'] == taxa_id:
            taxa['nome'] = data['nome']
            taxa['valor'] = data['valor']
            return jsonify({"message": "Taxa atualizada com sucesso!"}), 200
    return jsonify({"error": "Taxa não encontrada"}), 404

# Rota para excluir uma taxa existente
@app.route('/taxas/<int:taxa_id>', methods=['DELETE'])
def delete_taxa(taxa_id):
    for taxa in taxas:
        if taxa['id'] == taxa_id:
            taxas.remove(taxa)
            return jsonify({"message": "Taxa excluída com sucesso!"}), 200
    return jsonify({"error": "Taxa não encontrada"}), 404

# Implemente rotas semelhantes para outros recursos conforme necessário

if __name__ == '__main__':
    app.run(debug=True)
