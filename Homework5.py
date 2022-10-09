class Team:

    def __init__(self, nev, projekt, szerepkor):
        self._nev = nev
        self._projekt = projekt
        self._szerepkor = szerepkor
        print("-- Developer létrehozva --")

    def azon_projekt(self, masik):
        if isinstance(masik, Team):
            return self.projekt == masik.projekt

    @property
    def nev(self):
        return self._nev

    @property
    def projekt(self):
        return self._projekt

    @property
    def szerepkor(self):
        return self._szerepkor

    def __str__(self):
        return self.nev + " a "+str(self.projekt)+"-en dolgozik "+str(self.szerepkor)+" szerepkörben."


if __name__ == "__main__":
    
    peldany1 = Team("Ricsi", "SolArch", "Frontend")
    print(peldany1)

    peldany2 = Team("Angéla", "ZerTeng", "Tesztelő")
    print(peldany2)

    peldany3 = Team("Peti", "KefERP", "Backend")
    print(peldany3)

    peldany4 = Team("Éva", "KefERP", "Frontend")
    print(peldany4)
    
    contain= [peldany1,peldany2,peldany3,peldany4]
    for i in range(len(contain)):
        for j in range(len(contain)-i):
            if (contain[j+i].projekt==contain[i].projekt) & (contain[j+i].nev != contain[i].nev):
                print(contain[i].nev +" és "+contain[j+i].nev +" egy projekten dolgoznak")
                
            
            
    
    
    
