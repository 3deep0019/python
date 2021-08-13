# Case-8: Formatting class members using format()

class Person: 
   age=48 
   name="durga" 
print("{p.name}'s age is :{p.age}".format(p=Person())) 

# Output: durga's age is :48

class Person: 
 def __init__(self,name,age): 
     self.name=name 
     self.age=age 
print("{p.name}'s age is :{p.age}".format(p=Person('durga',48))) 
print("{p.name}'s age is :{p.age}".format(p=Person('Ravi',50))) 

# Note: Here Person object is passed as keyword argument. We can access by using its 
 #      reference variable in the template string