# we can give any name instead of self as they take by defaualt first argument as an instatnce
# but if we use @classmethod then the first instance would behave as class ,like here harsh is instance but as we put
# decrator @classmethod then it will become class and can change the value of class variable
class Employee:
   company="APPLE"

   @classmethod
   def changecompany(harsh, companyname):
       harsh.company = companyname

   def show(s):
    print(f'The name of employee is {s.name} and works in {s.company}')

e = Employee()
e.name="HARSH"
e.show()
e.changecompany("Tesla")
e.show()
print(Employee.company)
print(e.company)