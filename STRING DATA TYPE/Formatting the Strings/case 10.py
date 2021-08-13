#Case-10: Dynamic Float format template

num="{:{align}{width}.{precision}f}" 
print(num.format(123.236,align='<',width=8,precision=2)) 
print(num.format(123.236,align='>',width=8,precision=2)) 
'''
Output:
123.24
123.24
'''