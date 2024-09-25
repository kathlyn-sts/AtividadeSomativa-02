def calculadora(nome, operacao, num1, num2):
    if operacao not in ['+', '-', '*', '/']:
        raise ValueError("Operação inválida")

    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida")
        return num1 / num2
