# Q7) Write a Program for the following Requirement 
#     Input: a4b3c2
#     Output: aaaabbbcc

s=input("Enter Some String:") 
output='' 
for x in s: 
   if x.isalpha(): 
      output=output+x 
   previous=x 
else: 
   output=output+previous*(int(x)-1) 
print(output) 

# Note: chr(unicode)  The corresponding character
#       ord(character)  The corresponding unicode value
