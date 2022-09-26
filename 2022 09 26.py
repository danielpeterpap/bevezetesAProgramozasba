##def f():
##    return 4/0
##
##def g():
##    raise Exception("We call U.")
##
##def h():
##    try:
##        f()
##    except Exception as e:
##        print(e)
##    try:
##        g()
##    except Exception as e:
##        print(e)
##        
##if __name__ == "__main__":
##    h()
################################################################x
##raise Exception("Something went wrong.")
##raise RuntimeError("Runtime Error")
##from datetime import datetime
##
##class SuperError(Exception):
##    def __init__(self,message):
##        Exception.__init__(message)
##        self.when= datetime.now()
##raise SuperError("Something went wrong in class")

#####################################################################
##import sys
##
##randomList = ["a", 0 ,2]
##
##for entry in randomList:
##    try:
##        print("The entry is: ",entry)
##        r=1/int(entry)
##        break
##    except:
##        print("Oops!", sys.exc_info()[0], "occured")
##        print("Next entry.")
##        print()
##print("The reciprocal of ",entry," is: ", r)   ## only prints the first valid one!

######################################################################

##def fun(a):
##    if a >= 4:
##        b=a/(a-3)
##    print("The b value is: ",b)    
##try:    
##    fun(3)
##    fun(5)
##except ZeroDivisionError:
##    print("ZeroDivisionError occured and handled.")
##except NameError:
##    print("NameError occured and handled.")
##
##############################################################

try:
    k=5/0
    print(k)
except ZeroDivisionError:
    print("Can't divide by zero!")
finally:
    print("This always executes")
    k=5/0
    print(k)