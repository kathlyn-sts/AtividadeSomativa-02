def adicionar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return num1 / num2

def calculadora():
    nome = input('Digite seu nome: ')
    print(f'Bem-vindo à Calculadora, {nome}')

    operacao = input('Insira a operação matemática desejada (+, -, * or /): ')
    
    while True:
        try:
            num1 = float(input('Insira o primeiro número da operação: '))
            num2 = float(input('Insira o segundo número da operação: '))
            break
        except ValueError:
            print("Oops! Esse não era um número válido. Tente novamente...")

    if operacao == '+':
        print(adicionar(num1, num2))
    elif operacao == '-':
        print(subtrair(num1, num2))
    elif operacao == '*':
        print(multiplicar(num1, num2))
    elif operacao == '/':
        print(dividir(num1, num2))
