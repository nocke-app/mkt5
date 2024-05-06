# Função para aplicar o desconto com base no código inserido pelo cliente
def aplicar_desconto(codigo):
    # Dicionário de códigos de desconto e seus valores correspondentes
    codigos_desconto = {
        "Promo10": 0.10,
        "Promo20": 0.20,
        "Promo30": 0.30,
        "Promo40": 0.40
    }

    # Verificar se o código de desconto é válido
    if codigo in codigos_desconto:
        # Calcular o valor do desconto
        desconto = codigos_desconto[codigo]

        # Chame a função para aplicar o desconto na taxa de serviço
        taxa_de_servico = calcular_taxa_de_servico()
        taxa_de_servico_com_desconto = taxa_de_servico * (1 - desconto)

        # Aqui você pode adicionar a lógica para calcular o valor total com o desconto aplicado na taxa de serviço
        # Por enquanto, vamos apenas exibir uma mensagem para testar a funcionalidade
        print(f"Aplicando desconto de {desconto*100:.0f}% com código: {codigo}")
        print("Taxa de serviço com desconto:", taxa_de_servico_com_desconto)
        print("Desconto aplicado com sucesso!")
    else:
        # Se o código de desconto não for válido, exibir uma mensagem de erro
        print("Código de desconto inválido. Por favor, insira um código válido.")

# Função para calcular a taxa de serviço (exemplo)
def calcular_taxa_de_servico():
    # Aqui você colocaria a lógica real para calcular a taxa de serviço
    return 20.0  # Exemplo de taxa de serviço fixa de 20 unidades monetárias

# Simulando a entrada do cliente
codigo_desconto = input("Insira o código de desconto: ")

# Chamar a função para aplicar o desconto
aplicar_desconto(codigo_desconto)
