def calcular(num1, num2, ope):
    if ope == '+':
        return num1 + num2
    elif ope == '-':
        return num1 - num2
    elif ope == '*':
        return num1 * num2
    elif ope == '/':
        return num1 / num2
    else:
        raise ValueError("Operação inválida")

def main():
    x = input('Digite seu nome:  ')
    print('Bem-vindo à Calculadora, ' + x)

    ope = input('Insira a operação matemática desejada (+, -, * or /): ')

    while True:
        try:
            num1 = float(input('Insira o primeiro número da operação: '))
            num2 = float(input('Insira o segundo número da operação: '))
            break
        except ValueError:
            print("Oops!  Esse não era um número válido.   Tente novamente...")

    resultado = calcular(num1, num2, ope)
    print(resultado)

if __name__ == "__main__":
    main()
