class Szuperhos:
    def __init__(self,nev,szuperero = 50):
        self._nev = nev
        self._szuperero = szuperero
        ##print("Szuperhos letrehozva")
    ##def get_szuperero(self):
    ##    return self._szuperero
        
    ##def set_szuperero(self,ertek):
    ##    self._szuperero = ertek
    
    @property
    def szuperero(self):
        return self._szuperero
    
    @szuperero.setter
    def szuperero(self,ertek):
        self._szuperero = ertek
        
    def __str__(self):
        return self._nev + " Egy Szuperhos, akinek a szuper ereje "+str(self._szuperero)
    
    def __eq__(self,masik_hos):
        return self._nev == masik_hos._nev and self._szuperero == masik_hos._szuperero
    
    def __add__(self,masik_hos):
        if isinstance(masik_hos,Szuperhos):
            uj_szuperero= self._szuperero+masik_hos._szuperero
            uj_Szuperhos=Szuperhos("Megahős",uj_szuperero)
            return uj_Szuperhos
        else:
            return "no"
        
        
    
        
        
if __name__ == "__main__":
    hos1=Szuperhos("Thor",70)
    hos2=Szuperhos("Hulk",80)
    hos3=Szuperhos("Hulk",80)
    hos4=hos1 + hos2
    hos5=hos1+2
    
    ##hos1.set_szuperero(100)
    ##print(hos1.get_szuperero())
    #hos1.szuperero=100
    #print(hos1.szuperero)
    #print(hos2 == hos3)
    #print(hos4)
    print(hos5)
    
    
    
        