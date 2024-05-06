from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

saldo = 0

# Função para formatar o número para Reais (BRL)
def formatCurrency(number):
    return "{:.2f} BRL".format(number)

# Função para calcular a conversão do real para o dólar
def calculateUSDConversion(amountSent):
    exchangeRate = 5.0887  # Valor do dólar
    amountInUSD = amountSent / exchangeRate  # Convertendo o valor enviado para dólares
    return "{:.2f}".format(amountInUSD)  # Retornando o valor final em dólares com duas casas decimais

# Função para calcular a taxa de 5%
def calculateFee(amount):
    # Simulando uma taxa de 5% sobre o valor enviado
    return amount * 0.05

# Função para calcular o valor dos impostos (13,83% + 5%)
def calculateTaxes(amountSent):
    exchangeRate = 5.0887  # Valor do dólar
    amountInUSD = amountSent / exchangeRate  # Convertendo o valor enviado para dólares
    brazilianTaxesRate = 0.138283  # Taxa total de impostos brasileiros (PIS + COFINS + CSLL + IR)
    totalTaxesRate = brazilianTaxesRate + 0.05  # Soma da taxa de impostos brasileiros com a taxa de 5%
    taxesAmount = amountInUSD * totalTaxesRate  # Calculando o valor dos impostos
    return "{:.2f}".format(taxesAmount)  # Retornando o valor dos impostos com duas casas decimais

# Função para calcular o valor que o beneficiário irá receber em dólares
def calculateBeneficiaryReceives(amountSent):
    exchangeRate = 5.0887  # Valor do dólar
    amountInUSD = amountSent / exchangeRate  # Convertendo o valor enviado para dólares
    feeAmount = calculateFee(amountInUSD)  # Calculando a taxa de 5% sobre o valor convertido
    amountAfterFee = amountInUSD - feeAmount  # Subtraindo a taxa do valor em dólares
    return "{:.2f}".format(amountAfterFee)  # Retornando o valor final em dólares com duas casas decimais

# Função para calcular os créditos AWS
def calculateAWSCredits(sentAmount, feeAmount):
    valorF = sentAmount - feeAmount
    valorF2 = valorF * 0.002  # 0.2% da taxa Foxbit
    valorI = (valorF - valorF2) * (13.8283 / (100 + 13.8283))  # Cálculo dos impostos
    valorCreditosAWS = valorF - valorF2 - valorI
    return "{:.2f}".format(valorCreditosAWS)

# Função para atualizar o saldo
def updateSaldo(amount):
    global saldo
    saldo += float(amount)
    return "{:.2f}".format(saldo)

# Função para adicionar uma compra ao extrato
def addCompraToExtrato(amount):
    return "Compra no valor de USD {:.2f}".format(float(amount))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    sentAmount = float(request.form['amount-sent'])
    usdConversion = calculateUSDConversion(sentAmount)  # Calculando a conversão do Real para Dólar
    totalAmount = float(usdConversion) * (1 + 0.1383)  # Adicionando os 13,83% ao valor do dólar convertido
    formattedUSDConversion = "{:.2f}".format(float(usdConversion))  # Formatando o valor do dólar convertido com duas casas decimais
    formattedTotalAmount = "{:.2f}".format(totalAmount)  # Formatando o total com impostos com duas casas decimais
    return jsonify({'formattedUSDConversion': formattedUSDConversion, 'formattedTotalAmount': formattedTotalAmount})

@app.route('/confirmar', methods=['POST'])
def confirmar():
    sentAmount = float(request.form['amount-sent'])
    beneficiaryReceives = calculateBeneficiaryReceives(sentAmount)
    taxesAmount = calculateTaxes(sentAmount)
    awsCredits = calculateAWSCredits(sentAmount, float(taxesAmount))
    saldoAtualizado = updateSaldo(beneficiaryReceives)
    extrato = addCompraToExtrato(beneficiaryReceives)
    return jsonify({'saldoAtualizado': saldoAtualizado, 'extrato': extrato})

if __name__ == '__main__':
    app.run(debug=True)
