# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result

print("****** FAULTY CALCULATOR ******")
while(True):
    print("Enter the operator :\n 1.+\n2.-\n3.*\n4./\n5.exit")
    op=input()
    if (op =='1'or op=='+'):
        print("enter the first number: ")
        n1 = int(input())
        print("enter the second number: ")
        n2 = int(input())
        if((n1==56 and n2==9)or(n1==9 and n2==56) ):
            print("The sum is : 77")
        else:

            sum=n1+n2
            print("the sum is : ",sum)
    elif(op =='2'or op=='-'):
        print("enter the first number: ")
        n1 = int(input())
        print("enter the second number: ")
        n2 = int(input())
        sub=n1-n2
        print("the sub is :",sub)
    elif(op =='3'or op=='*'):
        print("enter the first number: ")
        n1 = int(input())
        print("enter the second number: ")
        n2 = int(input())
        if((n1==45 and n2==3)or(n1==3 and n2==45) ):
            print("the product is : 555")
        else:
            prod=n1*n2
            print("the product is : ",prod)
    elif(op=='4' or op =='/'):
        print("enter the first number: ")
        n1 = int(input())
        print("enter the second number: ")
        n2 = int(input())
        if(n1 == 56 and n2 == 6) :
            print("the division is : 4")
        elif(n2==0):
            print("division by zero is not possible")
        else:
            div=n1/n2
            print("the division is : ",div)
    elif(op=='5'or op=='exit'):
        print("--------------thanks------------------------")
        print(exit())




