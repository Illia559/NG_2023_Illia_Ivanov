def operation(operat):
    match operat:
        case "+": print(userNumber1 + userNumber2)
        case "-": print(userNumber1 - userNumber2)
        case "*": print(userNumber1 * userNumber2)
        case "/": print(userNumber1 / userNumber2)
                     
userNumber1 = float(input("Enter first number: "))
userNumber2 = float(input("Enter second number: "))
oper =str(input("Enter operation: "))
operation(oper)