# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern
def pypart(n):
    # outer loop to handle number of rows
    # n in this case
    for i in range(0, n):

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing stars
            print("* ", end="")

        # ending line after each row
        print("\r")


# Driver Code
n = 5
pypart(n)


# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern
def pypart(n):
	myList = []
	for i in range(1,n+1):
		myList.append("*"*i)
	print("\n".join(myList))

# Driver Code
n = 5
pypart(n)


#python3 code to print pyramid pattern using recursion
def pypart(n):
	if n==0:
		return
	else:
		pypart(n-1)
		print("* "*n)

# Driver Code
n = 5
pypart(n)
#this code is contributed by Shivesh Kumar Dwivedi


# python3 code to print pyramid pattern using while loop

# input
n = 5

i = 1;
j = 0
# while loop check the condition until the
# condition become false. if it is true then
# enter in to loop and print the pattern
while (i <= n):
    while (j <= i - 1):
        print("* ", end="")
        j += 1
    # printing next line for each row
    print("\r")
    j = 0;
    i += 1

# this code is contributed by gangarajula laxmi
