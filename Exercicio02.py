def leiaInt():
    try:
        numeroInt=int(input("Insira um numero inteiro: "))
        print("O número digitado foi:",numeroInt)
    except(ValueError,TypeError):
        print("Erro!!,Digite um numero inteiro valido!")
        leiaInt()
leiaInt()     

def leiaFloat():
    try:
        numeroFloat=float(input("Insira um numero real: "))
        print("O número digitado foi:",numeroFloat)

    except(ValueError,TypeError):
        print("Erro!!,Digite um numero real valido!")
        leiaFloat()
leiaFloat()       