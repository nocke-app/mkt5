import pandas as pd

# Função para ler o arquivo de texto e extrair os dados
def ler_arquivo_texto(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        dados = []
        pessoa = {}
        for linha in linhas:
            if linha.strip():  # Verifica se a linha não está em branco
                partes = linha.split(':')
                chave = partes[0].strip()
                valor = ':'.join(partes[1:]).strip()
                pessoa[chave] = valor
            else:
                if pessoa:
                    dados.append(pessoa)
                    pessoa = {}
        # Adiciona a última pessoa
        if pessoa:
            dados.append(pessoa)
    return dados

# Função para transferir os dados para o Excel
def transferir_para_excel(dados, nome_arquivo_excel):
    df = pd.DataFrame(dados)
    df.to_excel(nome_arquivo_excel, index=False)

# Nome do arquivo de texto de entrada
nome_arquivo_txt = 'dados.txt'

# Nome do arquivo Excel de saída
nome_arquivo_excel = 'dados.xlsx'

# Ler os dados do arquivo de texto
dados = ler_arquivo_texto(nome_arquivo_txt)

# Transferir os dados para o Excel
transferir_para_excel(dados, nome_arquivo_excel)

print("Dados transferidos para o Excel com sucesso!")
