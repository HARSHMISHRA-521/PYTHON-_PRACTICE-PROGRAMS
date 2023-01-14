for i in range(5):

    if i==3:
        break;
    print(i)
else:                          #this else will only execute only if the loop
                                   # completes or end completly and successfully
    print("loop in else")

# for counter in sequence:
#     #Statements inside for loop block
# else:
#     #Statements inside else block
#

for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")
