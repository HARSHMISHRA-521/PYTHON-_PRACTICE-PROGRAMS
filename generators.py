def my_generator():
    for i in range(5):
        yield i

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# Output:
# 0
# 1
# 2
# 3
# 4

print("\n")
gen = my_generator()
for i in gen:
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4