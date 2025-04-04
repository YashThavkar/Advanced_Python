'''
if you are trying to do something and you don't have a confidence about the result then you use
to avoid the killing of complete program we can use try except
if you got the error and there is still 200 lines left and its not going to run
but in try and except it is not going to throw the error it will try to handle the exceptions and try to move on...
'''

#try and except

try:
    open ("this.txt")

except Exception as e:
    pass  #pass permit the task to complete
    print(e)

# open("this.txt")

print("program is still alive")



###############################################################################################################

try:
    file = open("this.txt", 'r')

except EOFError as e:
    print("eof error")

except IOError as e:
    print("eo error")

finally:
    print("Its all done , perfectly")


#################################################################################################################

try:
    open("this.txt", 'r')

except Exception as e:
    print("there is an exception error which needs to solve")

else:
    print("there is no error occured  and the program is running well")

finally:
    print("we have reached till our results and gone trough all this...")
