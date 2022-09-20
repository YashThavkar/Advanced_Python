import bisect


no =83
# if i have to put 15 in the list where it should be in sorted manner only so how we should do

a = [1,2,30,55,63,84,92,107]

# hence it just show the postion where you can insert the number
print(bisect.bisect(a,no))

# to insert the number we will write
bisect.insort(a,no)
print(a)