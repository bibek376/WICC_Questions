# Explanation:
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

def High_Re_Occurance(list1):
    n=len(list1)//3
    list2=[]
    for i in range(len(list1)):
        count=0
        for j in range(len(list1)):
            if list1[i]==list1[j]:
                count=count+1
        if(count>=n):
            if (list1[i] in list2)==False:
                list2.append(list1[i])
    return list2

print(High_Re_Occurance([3,1,1,2,1,3,1,4,4,2,4]))
        
        