def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:
    print("I am always executed")
  # print("I am always executed")


x = func1()
print(x)

# The finally code block is also a part of exception handling. When we handle exception using the try
#  and except block, we can include a finally block at the end. The finally block is always executed,
# so it is generally used for doing the concluding tasks like closing file resources or closing database
# connection or may be ending the program execution with a delightful message.
#
# try:
# # statements which could generate
# # exception
# except:
# # solution of generated exception
# finally:
# # block of code which is going to
# # execute in any situation
#
# The finally block is executed irrespective of the
# outcome of try……except…..else blocks
# One
# of
# the
# important
# use
# cases
# of finally block is in a
# function
# which
# returns
# a
# value.
