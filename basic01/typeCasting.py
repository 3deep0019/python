# TYPE CASTING
# --- WE CAN CONVERT ONE DATA TYPE VALUE TO ANOTHER TYPE . this conversion  is called Taypecasting.

# 1 int()
a = int(123.986)
print(a)

b = int(True)
print(b)


c = int(False)
print(c)


# 2 flot()
f = float(10)
print(f)



#3 complex


# form 1 complex(x)
c = complex(10)
print(c)


# form 2 complex(x,y)
d = complex(10,2)
print(d)

f = complex(True,False)
print(f)

#4  bool()

a = bool(0)
b = bool(1)
c = bool(10)
d = bool(10.5)
e = bool(0.678)
print(a,b,c,d,e)

# 5 str()

a = str(10)
b = str(10.5)
c = str(10+5j)
d = str(True)
print(a,b,c,d)



# fondamental datatype VS Immutability

a = 10
b = 10
a is b 
print(True)
print(id(a))
print(id(b))




# byte data type 

x = [10,20,30,40,50,60,]
b = bytes(x)
print(type(b))
print(b[0])
print(b[-1])
for i in b  : print(i)


