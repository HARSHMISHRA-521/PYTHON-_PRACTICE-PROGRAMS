# a = 9
# b = 8
# c = sum((a, b)) # built in function

def function1(a, b):
    print("Hello you are in function 1", a+b)
    
def function2(a, b):
    """This is a function which will calculate average of two numbers
    this function doesn't work for three numbers"""
    average = (a+b)/2
    # print(average)
    return average

"""Docstring is a short form of documentation string. Its purpose is to give the programmer
 a brief knowledge about the functionality of the function. It must be the first string in a 
 function, and it is also an optional string but always good to have it while working on programs
  having multiple functions. The syntax for writing a docstring is very simple as it is just a string 
  written in between three double quotes placed three times (""" """) on either side of the string.
   But it has to be the first line of code in the function’s body. To call a docstring we write the 
   name of the function followed by ._doc_."""

# v = function2(5, 7)
# print(v)
print(function2.__doc__)
