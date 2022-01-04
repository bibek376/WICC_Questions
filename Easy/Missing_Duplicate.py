# Explanation:
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# 1st case

# Input :nums = [4,1,2,1,2]

# Output :4

def Missing_Duplicate(input):
    for i in range(len(input)):
        count=0
        for j in range(len(input)):
            if input[i]==input[j]:
                count=count+1
        if count==1:
            print(input[i])

nums=[4,1,2,1,2]
Missing_Duplicate(nums)