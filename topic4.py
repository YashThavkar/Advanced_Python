''' *args  and  **kwargs
#  *vars  and  **kvars
'''
###############################################################################################################
##ARGS

#def function_1(name, age , rollno):
#    print("The name of student is ",name , "and his age is ", age , "and the roll no is ", rollno)

#function_1("Yash" , 21 ,65)
#function_1("Fazle" , 20 ,22)
#NOTE :- here it uses as list


def function_1(*args):
    print(type(args))

    #if some time the information about student is not as followed then we can use a technique
    if(len(args)==3):
        print("The name of student is ",args[0] , "and his age is ", args[1] , "and the roll no is ", args[2])

    else:
        print("The name of student is ", args[0], "and his age is ", args[1])

#function_1("Yash" , 21 ,65)
#function_1("Fazle" , 20 )
list =["yash", 21]
function_1(*list)

#NOTE :- In args it uses tuple

################################################################################################################
##KWARGS

def marks(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)


marklist = {"fazle hasan": 9, "Jay Gholap": 9 , "Hritik Debnath" :8, "Ritvik Nimje": 7, "karan Modkundwar " :8,
            "yash Thavkar":6 ,"pranay Bobde":10}
marks(**marklist)


###############################################################################################################
### NORMAL ARGUMENTS , ARGS , KWARGS

def all(normal, *args, **kwargs):
    print(normal)

    for i in args:
        print(i)

    for key, value in kwargs.items():
        print(key, value)


list =['Yash', 21]

marklst = {"fazle hasan": 9, "Jay Gholap": 9 , "Hritik Debnath" :8, "Ritvik Nimje": 7, "karan Modkundwar " :8,
            "yash Thavkar":6 ,"pranay Bobde":10}

all("normal_arguments", *list,**marklst)

#if you use print statement then it will print none at last in output
#print(all("normal_arguments", *list,**marklst))