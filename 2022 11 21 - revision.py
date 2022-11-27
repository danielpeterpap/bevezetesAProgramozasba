def beolvas():
    list=[]
    try:
        with open("playlist.csv","r",encoding='utf-8') as f:
            sor=f.readline()
            while sor:
                darabolt=sor.split(";")
                dict = {"eloado" : darabolt[0] , "cim" : darabolt[1] , "mufaj" : darabolt[2] , "hossz" : int(darabolt[3])}
                list.append(dict)
                sor=f.readline()
    except FileNotFoundError as fnfe:
        print("File not found")
    return list

def teljes_hossz(list):
    ido=0
    for i in range(len(list)):
        ido+=list[i]["hossz"]
    perc=int(ido/60)
    ido=ido-60*perc
    
    with open("02_hossz.txt", "w") as f:
        text=str(perc)+" perc "+ str(ido)+ " masodperc"
        f.write(text)    

def leghosszabb_rockzene(lista):
    ido=0
    cime=""
    for i in range(len(list)):
        if(list[i]["mufaj"]=="rock"):
            if list[i]["hossz"] > ido:
                ido=list[i]["hossz"]
                cim=list[i]["cim"]
    with open("03_leghosszabb_rock.txt", "w") as f:
        f.write(cime)
        

def leggyakoribb_mufaj(lista):
    mufajok=""
    szamol=""
    darab=0
    for i in range(len(lista)):
        mufajok+=lista[i]["mufaj"]+" " 
    mufajok=mufajok.rstrip().split(" ")
    szamol=[[x,mufajok.count(x)] for x in set(mufajok)]
    for i in range(len(szamol)):
        if int(szamol[i][1]) > darab:
            darab = int(szamol[i][1])
            mufaj=szamol[i][0]
    mufaj=mufaj.upper()
    with open("04_kedvenc_mufaj.txt nevű ","w") as f:
        f.write(mufaj)

def zeneket_csoportosit(lista):
    szamol=""
    eloadok=""
    for i in range(len(lista)):
        eloadok+=lista[i]["eloado"]+" " 
    eloadok=eloadok.rstrip().split(" ")
    tuple=""
    for i in range(len(eloadok)):
        tuple=(i,0)
        szamol+=tuple
    for i in range(len(lista)):
        if szamol[0] ==i["eloado"]:
            
             
        
    
if __name__ == '__main__':
    zenelista=beolvas()
    #teljes_hossz(zenelista)
    #leghosszabb_rockzene(zenelista)
    #leggyakoribb_mufaj(zenelista)
    zeneket_csoportosit(zenelista)
    