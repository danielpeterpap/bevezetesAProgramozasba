#Írjunk egy programot, amely inch-ből cm-be és cm-ből inch-be tud konvertálni konzolról bekért értékeket.
# Kezeljük le azt is ha nem cm vagy inch mértékegységet kap, akkor a konzolra írassuk ki, hogy „Not correct unit!”. 


def Hazi(value,base):
    if(base=='inch'): #ha inch az alap,
        print(value*2.54) # szorozd 2,54-el hogy cm-t kapj
    else:
        if(base=='cm'): # ha cm az alap
            print(value/2.54) # osztasz ugyan ennyivel
        else:
            print("Not correct unit!") #ha egyik se, akkor a felhasználó nem ezt a programot keresi
    #done



if __name__ == "__main__":
    print("Adj meg egy számot és mértékegységet, külön sorokban (cm/inch)")
    value=float(input())
    base=str(input())
    Hazi(value,base)