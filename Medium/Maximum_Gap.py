# Explanation:

# Given an integer array nums, return the maximum difference between 
# two successive elements in its sorted form. If the array contains less than two elements, return 0.
# You must write an algorithm that runs in linear time and uses linear extra space.


# 1st case

# Input :nums = [3,6,9,1]
# Output :
# 3
# Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.


# 2nd case

# Input :nums = [10]
# Output :
# 0
# Explanation: The array contains less than 2 elements, therefore return 0.

def Max_Gap(nums):
    if len(nums)<2:
        return 0
    else:
        list1=[]
        sorted_nums=sorted(nums)
        for i in range(len(sorted_nums)):
            j=i+1
            if j<len(sorted_nums):
                list1.append(sorted_nums[j]-sorted_nums[i])
        return max(list1)

print(Max_Gap([3,6,9,1]))

            