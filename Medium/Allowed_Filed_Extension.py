# Explanation:
# In the document management system, you are now required to restrict files uploaded by users
# based on their extension.



# For eg: you only allow files with .pdf and .docx extensions. 


# Write pseudocode to implement this feature.

def Allowed_File_Extension(File_Name):
    Valid_Extension=['.pdf','.docs']
    for i in range(len(File_Name)):
        if "."==File_Name[i]:
            if File_Name[i:] in Valid_Extension:
                print("Extension Is Not Valid")
            else:
                print("Extension Is Not Valid")

Allowed_File_Extension("Allowed_Filed_Extension.py")