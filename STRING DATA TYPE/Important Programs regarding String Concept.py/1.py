# Q1) Write a Program to Reverse the given String
#  Input: durga
#  Output: agrud

#  Ans - 

# 1st Way:
s = input("Enter Some String:") 
print(s[::-1])

# 2nd Way:
s = input("Enter Some String:") 
print(''.join(reversed(s))) 

# 3rd Way:
s = input("Enter Some String:") 
i=len(s)-1 
target='' 
while i>=0: 
  target=target+s[i] 
i=i-1 
print(target)



