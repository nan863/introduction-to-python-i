def calculate(num1, operator, num2):
    if(operator == '+'):
        result = num1+num2
    elif(operator == '-'):
        result = num1-num2
    elif(operator == '*'):
        result = num1*num2
    elif(operator == '/'):
        result = num1/num2
    else:
        result = 'Operator is invalid'

    print(result)


cont = True

while cont:
    num1 = int(input("What is your first number? : "))
    operator = input("Operator : ")
    num2 = int(input("What is your second number? :"))
    calculate(num1, operator, num2)

    askCont = input('Do you want to continue?: (y/n)')
    if(askCont.lower() == 'y'):
        continue
    elif(askCont.lower() == 'n'):
        break