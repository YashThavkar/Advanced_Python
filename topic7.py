'''
Map

Reduce

Filter
'''

##################################################################################################################

'''                                            Map Function                                                     '''

#map(function _to_apply, list of inputs)

# l = [1,2,3,4,5,6]
# nl= []
# for i in l:
#     nl.append(i**2)
# print(nl)

'''with help of map function '''

def sq(i):
    return i**2

l= [1,2,3,4,5,6]
square = list(map(sq, l))
print(square)


##################################################################################################################

'''                                               Filter Functions                                                  '''

def greater_than_2(i):
    if i>100:
        return True
    else:
        return False

l =[1,2,3,4,5,54,45,356,56,56,45,546,46,436,35,35,235,34,46,456,545,445,4,657,445,745,34,53,254,87,978]
greater = list(filter(greater_than_2, l))
print(greater)


##################################################################################################################








