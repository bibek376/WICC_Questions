# Explanation:

# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, 
# due to some error, one of the numbers in s got duplicated to another number in the set, which results in 
# repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice or more and the number that is missing and return them in the form of 
# an array.


# 1st case

# Input :[1,2,2,4]
# Output :[2,3]

# 2nd case

# Input :[1,1,2,4]
# Output :[1,3]


def Missing_Number(Arr):
    final_result=[]
    Max_Value=max(Arr)
    count_num=[]
    count_num_freq=[]
    for i in range(1,Max_Value+1):
        count_num.append(i)
        count_num_freq.append(Arr.count(i))
    for j in range(len(Arr)):
        if count_num_freq[j]>1:
            final_result.append(count_num[j])
        if count_num_freq[j]==0:
            final_result.append(count_num[j])
    return final_result

print(Missing_Number([1,2,2,4]))

