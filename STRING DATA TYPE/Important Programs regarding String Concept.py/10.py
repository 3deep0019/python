# Q10) Write a Program to find the Number of Occurrences of 
#     each Character present in the given String?
#     Input: ABCABCABBCDE
#     Output: A-3,B-4,C-3,D-1,E-1

s=input("Enter the Some String:") 
d={} 
for x in s: 
 if x in d.keys(): 
    d[x]=d[x]+1 
else: 
  d[x]=1 
  for k,v in d.items(): 
    print("{} = {} Times".format(k,v)) 