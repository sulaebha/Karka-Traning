operand1=int(input("Enter the first number:"))
operator=input("Enter the operator:")
operand2=int(input("Enter the second number:"))
def arth_operation(operand1,operator,operand2):
    if operator=="+":
        operation=operand1+operand2
    elif operator=="-":
            operation=operand1-operand2
        
    elif operator=="*":
             operation=operand1*operand2
    
    elif operator=="/":
            operation=operand1/operand2
    elif operator=="%":
           operation=operand1%operand2
    elif operator=="**":
       operation=operand1**operand2

    else:
          print("invalid operator")
    

    # operation=operand1,operator,operand2
    return operation
operation=arth_operation(operand1,operator,operand2)
print(operation)

    