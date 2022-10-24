import string
def maganhangzo(a):
        done=""
        b=a.lower()
        mh=["a","á","e","é","i","í","o","ö","ő","ó","u","ú","ü","ű"]
        for i in b:
            if i not in mh:
                done+=i             
        return done
    
def irasjel_eltavolitas(szoveg):
        irasjel_nelkuli=""
        for karakter in szoveg:
            if karakter not in string.punctuation:
                irasjel_nelkuli+=karakter
        return irasjel_nelkuli

if __name__ == "__main__":
    #ss="Hello, world!"
    #tt=ss.upper()
    #print(tt)
    #jj=ss.capitalize()
    #print(jj)
    gyumolcs = "banán"
    #m=gyumolcs[1]
    #print(m)
    #lista=list(enumerate(gyumolcs))
    #print(lista)
    #hossz=len(gyumolcs)
    #print(hossz)
    #sz=len(gyumolcs)
    #utolso=gyumolcs[sz-1]
    #print(utolso)
    
    #i=0
    #while i<len(gyumolcs):
    #    karakter=gyumolcs[i]
    #    print(karakter)
    #    i+=1
    #for c in gyumolcs:
    #    print(c)
    #elotag="törp"
    #utotagok=["erős","költő","morgó","öltő","papa","picur","szakáll"]
    #for utotag in utotagok:
    #    p=elotag+utotag
    #    print(p)
    #s="A karib tenger kalózai"
    #print(s[0:1]) #A
    #print(s[2:14]) # karib tenger
    #print(s[15:22]) #kalózai
    #koszontes="Hello, vilag!"
    #uj_koszontes='J'+koszontes[1:]
    #print(uj_koszontes)
    #s="tesztelés a stringgel"
    #print(maganhangzo(s))
    
    #ss="Nos én sose csináltam mondta Alice"
    #szavak=ss.split()
    #print(szavak)
    #print(irasjel_eltavolitas(",.-fds.f,.bd.fg,erd,f.g,ewr.,df.gb,!%/=789+45613210%!/!%!+%/.ewrasfdfb.dgrt,esfa.d,bdf."))
    #s1="A nevem {0}!".format("Artúr")
    
    #print("i\ti**2\ti**3\ti**5\ti**10\ti**20")
    #for i in range(1,11):
    #    print(i,"\t",i**2,"\t",i**3,"\t",i**5,"\t",i**10,"\t",i**20,"\t",sep='')
        
    #elrendezes="{0:>4}{1:>6}{2:>6}{3:>8}{4:>13}{5:>24}" #better
    #print(elrendezes.format("i","i**2","i**3","i**5","i**10","i**20"))
    #for i in range(1,11):
    #    print(elrendezes.format(i,i**2,i**3,i**5,i**10,i**20))
    
    
    
    
    