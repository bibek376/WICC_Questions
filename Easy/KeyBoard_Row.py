# Explanation:
# Given an array of strings words, return the words that can be typed using letters of the alphabet on 
# only one row of American keyboard like the image below.


# In the American keyboard:

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

# 1st case

# Input :words = ["Hello","Alaska","Dad","Peace"]

# Output :["Alaska","Dad"]

def Keyboard_Row(checking_word):

    # American Standard keyboard
    row_first=set("qwertyuiop")
    row_second=set("asdfghjkl")
    row_third=set("zxcvbnm")

    key_value_dict=dict()
    
    # Creating Key Value Pair---->  {a:2,b:3,c:3,-----}
    for i in range(97,123):
        belongs=0
        if (chr(i) in row_first):
            belongs=1
        elif (chr(i) in row_second):
            belongs=2
        else:
            belongs=3
        key_value_dict[chr(i)]=belongs
    final_set=set()
    for j in checking_word:
        lower_value=j.lower()
        for char in lower_value:
            final_set.add(key_value_dict[char])
    if len(final_set)==1:
        return checking_word   

Words=["Hello","Alaska","Dad","Peace"]
Final_Output_List=[]
for i in range(len(Words)):
    if Keyboard_Row(Words[i]):
        Final_Output_List.append(Words[i])
print(Final_Output_List)
