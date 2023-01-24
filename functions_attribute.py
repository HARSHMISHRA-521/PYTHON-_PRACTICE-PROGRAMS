def average(a=5, b=2, c=1):
  print("The average is ", (a + b + c) / 2)
average(4, 6)
average(b=9)


def average1(*numbers):
  sum = 0
  for i in numbers:
    sum = sum + i
  print("Average is: ", sum / len(numbers))
  # return 7
  # return sum / len(numbers)
  print(type(numbers))

c = average1(5, 6, 7, 1)
print(c)


def name(**name):

  print("Hello,", name["fname"], name["mname"], name["lname"])
  print(type(name))

name(mname="Buchanan", lname="Barnes", fname="James")
