# Q -   How to Access Characters of a String?
# Ans - We can access characters of a string by using the following ways.

# 1) By using index
# 2) By using slice operator

# 1)Accessing Characters By using Index:
#  Python supports both +ve and -ve Index.
#  +ve Index means Left to Right (Forward Direction)
#  -ve Index means Right to Left (Backward Direction)

# s = 'durga'
# 1) >>> s='durga' 
# 2) >>> s[0] 
# 3) 'd' 
# 4) >>> s[4] 
# 5) 'a' 
# 6) >>> s[-1] 
# 7) 'a' 
# 8) >>> s[10] 
# 9) IndexError: string index out of range 
# Note: If we are trying to access characters of a string with out of range index then we will 
# get error saying: IndexError


# Q) Write a Program to Accept some String from the Keyboard and display its 
#  Characters by Index wise (both Positive and Negative Index)

s=input("Enter Some String:") 
i=0 
for x in s: 
   print("The character present at positive index {} and at nEgative index {} is {}".format(i,i-len(s),x)) 
i=i+1