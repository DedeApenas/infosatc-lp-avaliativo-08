def leiaInt(msg):
    verifica = False
    valor = 0
    while True:
        numero = str(input(msg))
        if numero.isnumeric():
            valor = int(numero)
            verifica = True
        else:
            print("Erro! Digite um número inteiro valido!")
        if verifica:
            break
    return valor        
numero = leiaInt("Digite um número: ")
print("O número digitado foi",numero)