# len() in-built Function:
#      -----------> We can use len() function to find the number of characters present in the string.

# Eg:

s = 'durga'
print(len(s)) 

# Q) Write a Program to access each Character of String in 
#    Forward and Backward Direction by using while Loop?

s = "Learning Python is very easy !!!" 
n = len(s) 
i = 0 
print("Forward direction") 
while i<n: 
 print(s[i],end=' ') 
 i +=1 
print("Backward direction") 
i = -1 
while i >= -n: 
 print(s[i],end=' ') 
 i = i-1 


# Alternative ways:
s = "Learning Python is very easy !!!" 
print("Forward direction") 
for i in s: 
    print(i,end=' ') 
print("Forward direction") 
for i in s[::]: 
     print(i,end=' ') 

print("Backward direction") 
for i in s[::-1]: 
 print(i,end=' ') 
