# Author: Brian Hoang
# Date: 10/30/2019
# Description: recursive function that finds the product of two positive integers together without using multiplication


#defines muliply function with two parameters(num1,num2)
def multiply(num1,num2):
    #if statement allows function to run until it reaches 1
    if num2 == 1:
        return num1
    #keeps adding num1 to itself with num2 amount of turns
    return multiply(num1,num2-1)+num1

#print(multiply(7,4))
