# Explanation:

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should 
# be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# 1st case

# Input :nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output :[1,2,2,3,5,6]

# 2nd case

# Input :nums1 = [1], m = 1, nums2 = [], n = 0
# Output :[1]

def Merge_Sorted_Array(Arr1,Arr2,m,n):
    Final_Result=[]
    i=0
    j=0
    k=0
    while(i<m and j<n):
        if(Arr1[i]<Arr2[j]):
            Final_Result.append(Arr1[i])
            i+=1
            k+=1
        else:
            Final_Result.append(Arr2[j])
            j+=1
            k+=1
    while(i<m):
        Final_Result.append(Arr1[i])
        i+=1
        k+=1
    while(j<n):
        Final_Result.append(Arr2[j])
        j+=1
        k+=1
    return Final_Result

List1=[1,2,3]
List2=[2,5,6]
m=len(List1)
n=len(List2)

print(Merge_Sorted_Array(List1,List2,m,n))