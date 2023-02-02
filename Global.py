# l = 10  # global
#
# print(l)
# def func(n):
#     # l = 5  # local
#     m = 8  # local
#     global l
#     l=l+45
#     print(l, m)
#     print(n, "I have printed")
#
#
# func("This is me ")
# print(l)
x = 89
def harsh():
    x= 20
    def harry():
        global x
        x =88
    print("before calling harry() ",x)
    harry()
    print("after calling harry()",x)

harsh()
print(x)
