x = input('Enter your name:  ')
print('Welcome to Calculator, ' + x)

ope = input('Enter the desired mathematical operation (+, -, * or /): ')

while True:
    try:
        num1 = float(input('Enter the first number of the operation: '))
        num2 = float(input('Enter the second number of the operation: '))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")