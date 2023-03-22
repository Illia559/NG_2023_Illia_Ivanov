def operation(operat):
    if operat == "+":
        result = userNumber1 + userNumber2
    elif operat == "-":
        result = userNumber1 - userNumber2
    elif operat == "*":
        result = userNumber1 * userNumber2
    elif operat == "/":
        result = userNumber1 / userNumber2
    return result



userNumber1 = float(input("Enter first number: "))
userNumber2 = float(input("Enter second number: "))
oper =str(input("Enter operation: "))
print (operation(oper))
