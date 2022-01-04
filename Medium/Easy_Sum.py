# find there easiest way to sum from 1 to 100 like 1+2+3+4+....+100=?

# Explanation:
# Anser is 5050. find simple way to calculate its sum


#Method 1
def Easy_Sum_Method_1(n):
    return n*(n+1)/2

print(Easy_Sum_Method_1(100))


#Method 2
def Easy_Sum_Method_2():
    sum=0
    for i in range(1,101):
        sum=sum+i
    return sum

print(Easy_Sum_Method_2())