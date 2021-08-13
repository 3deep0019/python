# Transfer Statements

# 1)break:
#     ------> We can use break statement inside loops to break loop execution based on some 
#           condition. 

for i in range(10): 
    if i==7: 
       print("processing is enough..plz break") 
    break
print(i)

cart=[10,20,600,60,70] 
for item in cart: 
 if item>500: 
   print("To place this order insurence must be required") 
 break 
print(item) 