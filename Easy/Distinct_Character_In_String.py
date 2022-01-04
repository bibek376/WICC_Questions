# Distinct Characters In String | Using array and loop only
#You have to create a program using any programming languages to find the distinct characters in a string.

# 1st case

# Input :cricket

# Output :
# {c,r,i,k,e,t}

# 2nd case

# Input :developer

# Output :{d,e,v,l,o,p,r}

def Distinct_Character_In_String(string):
    lwr_string=string.lower()
    list1=[]
    for i in range(len(string)):
        if(lwr_string[i] in list1) == False:
            list1.append(lwr_string[i])
    return list1

#Function Call
input_string="developer"
print(Distinct_Character_In_String(input_string))



