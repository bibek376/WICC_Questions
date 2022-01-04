# Explanation:

# Given an unsorted integer array nums, return the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses constant extra space.

# 1st case

# Input :[1,2,0]
# Output :3

# 2nd case

# Input :[3,4,-1,1]
# Output :2

def First_Missing_Positive(list1):
    count_num=[]
    count_num_freq=[]
    for i in range(min(list1),max(list1)+2):
        count_num.append(i)
        count_num_freq.append(list1.count(i))
    for j in range(len(count_num_freq)):
        if (count_num_freq[j]==0) and (count_num[j]>0):
            return count_num[j]

print(First_Missing_Positive([3,4,-1,1]))

