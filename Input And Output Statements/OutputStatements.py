# form 1 ------> To print new line character


# form 2 ---------> print(string)
   #     -----------> In the string we can use escape character also.print

print("hello\nmanish") 

# string repeation operator * ---> 'manish'*3 or 3*"manish"

# string concatenation operator also +
#        ------> both arguments should be string type.
print(3*'manish'+'pathak')
print("manish" +"pathak")


#   Q what is the diff b/t the following line.



# form 3 -------> print with variable number of argument or sep attribute.
#   *** defolte value for sep attribute space.
a,b,c =10,20,30
print("the value are:",a,b,c)


name = "manish"
gf = "mal"
print('hello',name,'your girlfriend',gf,'is tooo hote')

a,s,d,=10,20,30
print(a,s,d,sep='-')


#   from ---> print() with end attribute other than \n if you want any othher character then use end attribute.

print("hello",end=' ')
print("manish",end=' ')
print("soft")

a,b,c=10,20,30
print(a,b,c,sep='*')
print(a,b,c,sep='-')


a,b,c=10,20,30
print(a,b,c,sep='*',end='####')
print(a,b,c,sep='-')
print(a,b,c,end=' ')



#   form 5    --> print(object) statement
l=[10,20,30,40,]
t=[10,20,30,40,]
print(l)
print(t)

# form 6  ---> print (formatted string)

#  %i ----> int ,   %d---> INT , %f ---> float  , %s  ---> string
# 
 #print("formatted string"  %(variable list))

#  a = 10
#  print("a value is % i'%a")
  

#   form 7   ---> print() with replacement operator { }
#                                                        {  } --->  replacement operator

name = 'manish'
salary = 19999999
gf = "sunny"
print("hello {x}, your salary is {y}, and tour friend {z}, is waiting ".format(x=name,y=salary,z=gf))


name = 'manish'
salary = 19999999
gf = "sunny"
print("hello {0} your salary is {1} and tour friend {2} is waiting ".format(name,salary,gf))