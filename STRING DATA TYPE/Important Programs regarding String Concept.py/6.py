# Q6) Write a Program to Sort the Characters of the String and 
#     First Alphabet Symbols followed by Numeric Values
#     Input: B4A1D3
#     Output: ABD134

s=input("Enter Some String:") 
s1=s2=output='' 
for x in s: 
 if x.isalpha(): 
    s1=s1+x 
 else: 
    s2=s2+x 
for x in sorted(s1): 
    output=output+x 
for x in sorted(s2): 
    output=output+x 
print(output) 
