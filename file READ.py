f = open("HARSH.txt", "rt")
print(f.readlines())  # prints the list of lines
print(f.readline())
print(f.readline())
print(f.readline())
content = f.read()

for line in f:
    print(line, end="")
print(content)
# content = f.read(34455)
# print("1", content)
#
# content = f.read(34455)
# print("2", content)
f.close()
