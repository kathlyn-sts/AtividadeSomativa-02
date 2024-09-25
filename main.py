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
               
            
if ope in ['+']:
    print(num1+num2)
    
if ope in ['-']:
    print(num1-num2)

if ope in ['*']:
    print(num1*num2)

if ope in ['/']:
    print(num1/num2)