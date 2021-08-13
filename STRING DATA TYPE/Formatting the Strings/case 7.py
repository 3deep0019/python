
#Case-7: Formatting dictionary members using format()

person={'age':48,'name':'durga'} 
print("{p[name]}'s age is: {p[age]}".format(p=person)) 
'''
Output:
durga's age is: 48

Note: p is alias name of dictionary
      person dictionary we are passing as keyword argument

More convinient way is to use **person

'''
person={'age':48,'name':'durga'} 
print("{name}'s age is: {age}".format(**person)) 

# Output: durga's age is: 48