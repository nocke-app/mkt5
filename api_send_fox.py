import requests
import time
import hashlib

# Função para autenticar o usuário na API da Foxbit
def autenticar(userId, apiKey, secretKey):
    nonce = str(int(time.time() * 1000))
    userInfo = f"{nonce}{userId}{apiKey}"
    signature = hashlib.sha256(secretKey.encode('utf-8')).update(userInfo.encode('utf-8')).hexdigest()
    return nonce, signature

# Função para enviar o saldo de créditos da conta do usuário para a Foxbit
def enviar_saldo_creditos(userId, apiKey, secretKey, accountId, omsId, saldo_creditos, login_foxbit_destino):
    nonce, signature = autenticar(userId, apiKey, secretKey)
    url = f"https://api.foxbit.com.br/SendOrder"
    data = {
        "userId": userId,
        "apiKey": apiKey,
        "accountId": accountId,
        "omsId": omsId,
        "nonce": nonce,
        "signature": signature,
        "orderType": "credit_transfer",
        "amount": saldo_creditos,
        "destination_login": login_foxbit_destino
    }
    response = requests.post(url, json=data)
    return response.json()

# Exemplo de uso:
def exemplo_integracao():
    userId = 82127
    apiKey = "nK6L041FG4h1boWlW1EYlXlN99U5zrGFtEPiRmNl"
    secretKey = "lNmRiPEtFGrz5U99NlXlYE1WlWob1h4GF140L6Kn"
    accountId = 12345  # ID da conta do usuário na Foxbit
    omsId = 67890  # ID do Sistema de Gerenciamento de Pedidos
    saldo_creditos = 100.0  # Valor do saldo de créditos a ser enviado
    login_foxbit_destino = "login_foxbit_destino"  # Login da conta Foxbit destino

    resposta_envio = enviar_saldo_creditos(userId, apiKey, secretKey, accountId, omsId, saldo_creditos, login_foxbit_destino)
    print(resposta_envio)

# Chamada da função de exemplo
exemplo_integracao()
