def calculadora(num1=None, num2=None, ope=None):
    if num1 is None or num2 is None or ope is None:
        nome = input("Qual é o seu nome? ")
        ope = input(f"{nome}, qual operação deseja realizar (+, -, *, /)? ")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

    if ope == "+":
        return num1 + num2
    elif ope == "-":
        return num1 - num2
    elif ope == "*":
        return num1 * num2
    elif ope == "/":
        if num2 == 0:
            raise ZeroDivisionError("Não é possível dividir por zero")
        return num1 / num2
    else:
        raise ValueError("Operação inválida")
