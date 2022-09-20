'''
lambda function

lambda argument: manipulate(argument)

'''

def num(a,b):
    return a+b

print(num(4,5))

# or
def num1(x,y):
    c = x+y
    return c

print(num1(12,546))

###################################################################################################################

''' Now we will try it with help of lambda function'''
add = lambda x,y : x/y
print(add(14,56))