# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20
# Explanation:
# Summation should like 8+2+3+0+7 = 20


def addition(l):
    sum=0
    for i in l:
        sum=sum+i
    return sum
l=[8, 2, 3, 0, 7]
print (addition(l))





