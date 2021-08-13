# Case-9: Dynamic Formatting using format()

string="{:{fill}{align}{width}}" 
print(string.format('cat',fill='*',align='^',width=5)) 
print(string.format('cat',fill='*',align='^',width=6))
print(string.format('cat',fill='*',align='<',width=6)) 
print(string.format('cat',fill='*',align='>',width=6)) 

'''
Output:
*cat*
*cat**
cat***
***cat

'''