#Explanation
# The provided code implements the Apriori algorithm,
# a popular algorithm for frequent itemset mining. Here's an explanation of the code:
#
# The code starts by defining the dataset, which is a list
# of transactions. Each transaction is represented as a list of items.
#
# The init list is initialized to store all unique items present in
# the dataset. This is done by iterating over each transaction and adding the unique items to the init list.
#
# The sp variable represents the support threshold as a percentage.
# It is used to determine the minimum support count required for an itemset to be considered frequent.
#
# The c Counter is initialized to keep track of the count of each item in the dataset.
#
# The code calculates the count of each item by iterating over the
# dataset and incrementing the count for each item encountered.
#
# The l Counter is initialized to store the frequent itemsets.
# It filters the items from c that have a count greater than or equal
# to the support threshold (s) and stores them as frequent itemsets.
#
# The code then enters a loop to iteratively generate larger frequent
# itemsets. It starts with count = 2 and continues until no more frequent itemsets are found.
#
# In each iteration of the loop, the code generates candidate itemsets
# (nc) by combining the frequent itemsets from the previous iteration.
#
# The count of each candidate itemset is calculated by iterating
# over the dataset and checking if the candidate itemset is a subset
# of each transaction. The count is incremented for each transaction where the candidate itemset is found.
#
# The code filters the candidate itemsets (nc) based on the support
# threshold and stores them as frequent itemsets in l.
#
# If no frequent itemsets are found in an iteration, the loop is terminated.
#
# Finally, the code prints the resulting frequent itemsets.
#
# The code then performs association rule mining on the frequent itemsets.
# It iterates over each frequent itemset and generates all possible subsets of the itemset.
#
# For each subset, the code calculates the confidence of the association
# rule by dividing the count of the frequent itemset by the count of the subset.
#
# The code prints the association rules along with their confidence.
#
# The code essentially applies the Apriori algorithm to find frequent
# itemsets and mine association rules from a given dataset.


from itertools import combinations
from collections import Counter

# Define the dataset
data = [
    ['T100', ['I1', 'I2', 'I5']],
    ['T200', ['I2', 'I4']],
    ['T300', ['I2', 'I3']],
    ['T400', ['I1', 'I2', 'I4']],
    ['T500', ['I1', 'I3']],
    ['T600', ['I2', 'I3']],
    ['T700', ['I1', 'I3']],
    ['T800', ['I1', 'I2', 'I3', 'I5']],
    ['T900', ['I1', 'I2', 'I3']]
]

# Generate initial itemset
init = []
for i in data:
    for q in i[1]:
        if q not in init:
            init.append(q)
init = sorted(init)
print("Initial Itemset (C1):", init)

# Set minimum support threshold
sp = 0.4
s = int(sp * len(init))

# Generate frequent itemsets of size 1 (L1)
c = Counter()
for i in init:
    for d in data:
        if i in d[1]:
            c[i] += 1
print("C1:")
for i in c:
    print(str([i]) + ": " + str(c[i]))
print()

l = Counter()
for i in c:
    if c[i] >= s:
        l[frozenset([i])] += c[i]
print("L1:")
for i in l:
    print(str(list(i)) + ": " + str(l[i]))
print()

pl = l
pos = 1

# Generate frequent itemsets of size greater than 1
for count in range(2, 1000):
    nc = set()
    temp = list(l)
    for i in range(0, len(temp)):
        for j in range(i + 1, len(temp)):
            t = temp[i].union(temp[j])
            if len(t) == count:
                nc.add(temp[i].union(temp[j]))
    nc = list(nc)

    c = Counter()
    for i in nc:
        c[i] = 0
        for q in data:
            temp = set(q[1])
            if i.issubset(temp):
                c[i] += 1
    print("C" + str(count) + ":")
    for i in c:
        print(str(list(i)) + ": " + str(c[i]))
    print()

    l = Counter()
    for i in c:
        if c[i] >= s:
            l[i] += c[i]
    print("L" + str(count) + ":")
    for i in l:
        print(str(list(i)) + ": " + str(l[i]))
    print()

    if len(l) == 0:
        break
    pl = l
    pos = count

# Print the final result
print("Final Result (Frequent Itemsets):")
print("L" + str(pos) + ":")
for i in pl:
    print(str(list(i)) + ": " + str(pl[i]))
print()

# Generate association rules
for l in pl:
    c = [frozenset(q) for q in combinations(l, len(l) - 1)]
    mmax = 0
    for a in c:
        b = l - a
        ab = l
        sab = 0
        sa = 0
        sb = 0
        for q in data:
            temp = set(q[1])
            if a.issubset(temp):
                sa += 1
            if b.issubset(temp):
                sb += 1
            if ab.issubset(temp):
                sab += 1
        temp = sab / sa * 100
        if temp > mmax:
            mmax = temp
        temp = sab / sb * 100
        if temp > mmax:
            mmax = temp
        print(str(list(a)) + " -> " + str(list(b)) + " = " + str(sab / sa * 100) + "%")
        print(str(list(b)) + " -> " + str(list(a)) + " = " + str(sab / sb * 100) + "%")
    curr = 1
    print("Choosing:", end=' ')
    for a in c:
        b = l - a
        ab = l
        sab = 0
        sa = 0
        sb = 0
        for q in data:
            temp = set(q[1])
            if a.issubset(temp):
                sa += 1
            if b.issubset(temp):
                sb += 1
            if ab.issubset(temp):
                sab += 1
        temp = sab / sa * 100
        if temp == mmax:
            print(curr, end=' ')
        curr += 1
        temp = sab / sb * 100
        if temp == mmax:
            print(curr, end=' ')
        curr += 1
    print()
    print()