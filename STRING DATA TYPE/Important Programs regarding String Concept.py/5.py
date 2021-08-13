# Q5) Program to Merge Characters of 2 Strings into a Single 
#     String by taking Characters alternatively

#     Input: s1 = "ravi"
#     s2 = "reja"
#     Output: rtaevjia

s1=input("Enter First String:") 
s2=input("Enter Second String:") 
output='' 
i,j=0,0 
while i<len(s1) or j<len(s2): 
 if i<len(s1): 
    output=output+s1[i] 
    i+=1 
 if j<len(s2): 
    output=output+s2[j] 
    j+=1 
print(output) 