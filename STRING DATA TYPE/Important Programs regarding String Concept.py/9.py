# Q9) Write a Program to Remove Duplicate Characters from 
#     the given Input String?
#     Input: ABCDABBCDABBBCCCDDEEEF
#     Output: ABCDEF
s = input("Enter Some String:") 
l=[] 
for x in s: 
    if x not in l: 
       l.append(x) 
output=''.join(l) 
print(output)