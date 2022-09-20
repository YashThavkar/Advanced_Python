'''
Format Function
'''

users = ['fazle', 'hritik', 'jayvardhan', 'karan', 'pranay', 'ritvik', 'yash']

system = ['linux', 'rarpberry pi', 'ios', 'windows', 'ios', 'kali', 'linux']


# to get the output like this we naturally use this technique

# for i in range (0, len(users)):
#     print("System used by" , users[i] , "is" ,system[i])



# but we are extraodinary persons yane ki mentos zindagi

for i in range (0, len(users)):
    temp = "computer used  by {} is {} ".format(users[i], system[i])
    print(temp)

#there is a new technique we can spilt the line in print statement

for i in range(0, len(users)):
    temp = "System used by {} is {}"
    print(temp.format(users[i], system[i]))

#here we can  change the format

for i in range(0, len(users)):
    temp = "System used by {1} is {0}"
    print(temp.format(users[i], system[i]))