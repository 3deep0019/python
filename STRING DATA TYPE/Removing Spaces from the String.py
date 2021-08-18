# Removing Spaces from the String:

# We can use the following 3 methods

# 1) rstrip()  To remove spaces at right hand side
# 2) lstrip() To remove spaces at left hand side
# 3) strip()  To remove spaces both sides

city=input("Enter your city Name:") 
scity=city.strip() 
if scity=='Hyderabad': 
 print("Hello Hyderbadi..Adab") 
elif scity=='Chennai': 
 print("Hello Madrasi...Vanakkam") 
elif scity=="Bangalore": 
 print("Hello Kannadiga...Shubhodaya") 
else: 
 print("your entered city is invalid") 

# Finding Substrings:
# We can use the following 4 methods

# For forward direction:
# 1) find()
# 2) index()

# For backward direction:
# 1) rfind()
# 2) rindex()
