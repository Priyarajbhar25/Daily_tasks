#Defining try block for exception handling
try :
    #Taking values from user
    number1=int(input("Enter first number"))
    number2=int(input("Enter second number"))
    result=number1/number2
    #Display result if right
    print(result)

##Defining except block handles exceptions that are raised in the try block
except ZeroDivisionError :
    #Display when the exception will occur
    print("Cannot divide by zero")

