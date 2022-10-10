
import math


def prime(a):
    for i in range(int(math.sqrt(a))):
        if a%(i+2) == 0:
            return False
        else:pass
        
    return True   

def RPS(a,b):
    a=str(a)
    a=a.lower()
    b=str(b)
    b=b.lower()
    
    if a==b:
        return "döntetlen"
    
    if ((((a=="kő") & (b=="papír")) | ((a=="papír") & (b=="kő"))) |((a=="olló") & (b=="papír"))):
        return "Az első játékos nyert"
    else:
        return "A Második játékos nyert"

def fib(a):
    i = 1
    if a == 0:
        fib = []
    elif a == 1:
        fib = [1]
    elif a == 2:
        fib = [1,1]
    elif a > 2:
        fib = [1,1]
        while i < (a - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
            
    for i in range(len(fib)):
        print(fib[i])
        
    
def legs(a,b,c):
    return a*2+(b+c)*4



if __name__ == "__main__":
    ##print(prime(int(input("Adj meg egy számot, amiről rudni akarod, hogy prím-e"))))
    ##print("-------")
    ##p1=input("Első játékos.Add meg mit mutatsz! (kő, papír vagy olló)")
    ##p2=input("Második játékos.Add meg mit mutatsz! (kő, papír vagy olló)")
    ##print(RPS(p1,p2))
    ##print("--------")
    fibN=int(input("mennyi fibonacci számot generáljak? "))
    fib(fibN)
    ##print("--------")
    ##csirke=int(input("Mennyi csirke van? "))
    ##tehén=int(input("Mennyi tehén van? "))
    ##malac=int(input("Mennyi malac van? "))
    ##print(legs(csirke, tehén, malac))
    ##print("--------")
    ##
    ##age=int(input("Hány éves a gyerek?"))
    ##print(max(range(0,(age+1))))
    
    