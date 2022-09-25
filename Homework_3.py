
from ast import And


def Hazi(A,B,C):
    if ((A+B)>=C) and ((A+C) >= B) and ((B+C) >= A): ## ha bármely 2 oldal nagyobb vagy egyenlő a harmadik oldalnál
        print("A/Az ",A,", ",B," és ",C," oldalú háromszög megszerkeszthető") ## a háromszőg megszerkeszthető
    else:
        print("A/Az ",A,", ",B," és ",C," oldalú háromszög NEM megszerkeszthető") ## ellenkező esetben nem



if __name__ == "__main__":
    print("Adja meg a háromszög 3 oldalát cm-ben:")
    A=input("A oldal (CM):")
    B=input("B oldal (CM):")
    C=input("C oldal (CM):")
    
    Hazi(A,B,C)