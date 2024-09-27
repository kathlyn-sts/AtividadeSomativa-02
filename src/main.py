# src/main.py

def calculadora(num1, num2, ope):
    if ope == '+':
        return num1 + num2
    elif ope == '-':
        return num1 - num2
    elif ope == '*':
        return num1 * num2
    elif ope == '/':
        if num2 == 0:
            raise ValueError("Não é possível dividir por zero")
        return num1 / num2
    else:
        raise ValueError("Operação inválida")
