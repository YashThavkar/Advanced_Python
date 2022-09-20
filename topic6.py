'''
List Comprehension
Dictionary Comprehension
Set Comprehension
Generator Comprehension
'''
################################################################################################################

'''                                            List Comprehension                                                  '''
#i will write a code for numbers in the list are divisible by 3 or not if then we add it in one new list

list =[1,34,345,45,456,7567,88,5878,7,67,88,879,79,7546,65,635,4,523,4,124,5435,46,45,7,674,6,3,7,7,57,564,63,5523,55,2,45,445,4,25]
divisible_by_3= []

for i in list:
    if i %3==0:
        divisible_by_3.append(i)

print( " this code was written without help of comprehension ", divisible_by_3)

print( " this code is written with help of comprehension     ",  [i for i in list if i%3==0 ])
# print([ i for i in list if i%3==0])

################################################################################################################

'''                                        Dictionary Comprehension                                               '''

dic1= { 'a':3, 'b' :5 , 'A' :19, 'B' :21 , 'c' :17}
# i will try to merge the same alphabets which differs from each others as lower and upper space

print({i.lower():dic1.get(i.lower(), 0) + dic1.get(i.upper(),0) for i in dic1.keys()})



################################################################################################################

'''                                            Set Comprehension                                                   '''

set = {i**2 for i in [1,2,2,2,4,3,4,3,4,4,6,7,6,9,7,8,1,1,4,4,5,5,9,9,8,9,7,5,6,4,3,5,6,4,5,5,4,4,3] if i%3==0}
print(set)


################################################################################################################

'''                                           Generator Comprehension                                              '''

gen = (i for i in range(41) if i%4==0)
for items in gen:
    print(items)