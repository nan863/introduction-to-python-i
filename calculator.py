num1 = int(input("What is your first number? : "))
operator = input("Operator : ")
num2 = int(input("What is your second number? :"))

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