
# f= open("harsh.txt","a")
# f.write("harsh bhaiya bahut acche hain\n")
# a=f.write("harsh bhaiya bahut acche nahi hain\n")
# print(a)
# f.close()
# f= open("harsh.txt","a")
# f.write("harsh bhaiya  acche nahi hain\n")
# f.close()
# f= open("harsh.txt","r+")
# f.write("harsh mishra hai mera naam\n")
# f.close()


# g = open("harsh1.txt","r+")
# g.write("harsh mishra hai mera naam\n")
# g.close()
g = open("harsh1.txt ","w")
g.write("write harsh \t")
g.close()
# g = open("harsh1.txt ","a")
# g.write("append harsh")
# g.close()

g = open("harsh1.txt","r+")
# print(g.read())
g.write("harsh mishra hai mera naam\n")
print(g.__dict__)
g.close()
# g = open("harsh1.txt ","w")
# # print(g.read())
# g.write("write harsh 22222 \t")
# g.close()

#writing method for iterable objects
f = open('myfile.txt', 'w')
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    f.write(line + '\n')
f.close()

f = open('myfile.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()
