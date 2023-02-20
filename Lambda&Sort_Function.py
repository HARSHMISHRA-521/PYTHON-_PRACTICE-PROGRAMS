#lambda functions or anonymous function

# def minus(x, y):
#     return x - y

   # or

# minus  = lambda x ,y : x -y
#
# print(minus(9,4))

#sort() function

# list.sort(reverse=True|False, key=myFunc)

# reverse	Optional. reverse=True will sort the list descending. Default is reverse=False
# key	Optional. A function to specify the sorting criteria(s)

# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)


# Sort a list of dictionaries based on the "year" value of the dictionaries

# A function that returns the 'year' value:
def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)
print(cars)

