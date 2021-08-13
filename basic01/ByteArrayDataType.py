# ---bytearray is exactly same as bytes data type except thst itd element can be modified

x=[10,20,30,40,50,]
b=bytearray(x)
for i in b : print(i)
b[1]=100
for i in b: print(i)
