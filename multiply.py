def multiply(num1,num2):
    if num2 == 1:
        return num1

    return multiply(num1,num2-1)+num1

#print(multiply(7,4))
