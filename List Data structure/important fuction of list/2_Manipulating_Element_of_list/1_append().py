#1) append() Function:
#    ------------->   We can use append() function to add item at the end of the list.
list=[] 
list.append("A") 
list.append("B") 
list.append("C") 
print(list) 


#Eg: To add all elements to list upto 100 which are divisible by 10

list=[] 
for i in range(101): 
     if i%10==0: 
      list.append(i) 
print(list) 