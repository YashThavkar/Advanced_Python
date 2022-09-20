'''
Advanced Slicing
'''

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(l[2:7])
# always remember the no. of output at this program will be 7-2=5

# remember whenever you slice the list from backside you should keep greater number
# first with negative sign and then small number to reached till the number

print(l[-7:-2])
print(l[:-5])

'''now we will try to find out alternate number in the list'''
print(l[::2])

'''now we will reverse the list'''
print(l[::-1])
