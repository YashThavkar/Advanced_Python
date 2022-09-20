'''
Iterable- An iteratable is a Python object that can be used as a sequence.
          You can go to the next item of the sequence using the next () method.

Iterator- An iterator is an object that contains a countable number of values.
          An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Iteration- Getting to next element and try to fetch the element known as iteration

'''

'''
GENERATORS :- where it should not print the numbers but able to store the specific numbers in it

We can make generators before using it and later on  we can use it..
It is used for one time (single iteration)
'''

# for i in range(1000):
#     print(i)

def gen(n):
    for i in range(n):
        yield i

# print(gen(10000000))
# for i in gen(1000000):
#     print(i)

'''we will try to find really generators get iterate single time'''

obj1 = gen(4)
'''if i try here no. 4 then it will give error after 4 space'''
print(next(obj1))
print(next(obj1))
print(next(obj1))
print(next(obj1))
print(next(obj1))
print(next(obj1))
print(next(obj1))
print(next(obj1))
print(next(obj1))