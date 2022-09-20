'''
Enumerated Function
'''

a = ['fazle', 'hritik', 'jayvardhan', 'karan', 'pranay', 'ritvik', 'yash']

# i have to write the code where the output will be of postion which is divisible by 2

# j = 0
# for i in a:
#     j= j+1
#     if j%2==0:
#         print(i)

#this will be our output after 10 min

#now we will try to learn with mentos zindagi

for i , j in enumerate(a):
    if (i+1):
        print(i, j)


for i , j in enumerate(a):
    if (i+1) % 3 == 1:
        print(j)




















