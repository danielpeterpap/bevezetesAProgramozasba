

#try:
#    file = open("be.txt","r",encoding="UTF8" )
#
#    tartalom = file.readlines()
#
#    for sor in tartalom:
#        sor=sor.rstrip()
#        print(sor)
#
#    file.close
#    atlag=0
#    with open("be.txt","r",encoding="UTF8") as f:
#        osszeg=0
#        darab=0
#        sor=f.readline()
#        
#        while sor:
#            osszeg+=int(sor)
#            darab+=1
#            sor=f.readline()
#        atlag=osszeg/darab
#    
#    with open("ki.txt","w",encoding="UTF8") as f:
#        f.write("Az átlag "+str(atlag)+"\n")
#        
#except FileNotFoundError as fnfe:
#    print("File not found")
#
#n=int(input("hány sort Olvassak?"))
#try:
#    with open("be.txt","r",encoding="UTF8") as f:
#        for i in range(n):
#            print(f.readline().rstrip())
#except FileNotFoundError as fnfe:
#    print("File not found")
#leghosszabb=0
#megoldas=""
#try:
#    with open("leghosszabb.txt","r",encoding="utf-8") as f:
#        sor = f.readline().rstrip()
#        while sor:
#            a=sor.split(" ")
#            for b in a:
#                if len(b)>leghosszabb:
#                    leghosszabb=len(b)
#                    megoldas=b
#            sor=f.readline().rstrip()
#    print(megoldas)
#except FileNotFoundError as fnfe:
##    print("File not found")
#full=""
#try:
#    with open("be.txt","r",encoding="UTF8") as f:
#        sorSzam=1
#        sor=f.readline()
#        
#        while sor:
#            if sorSzam == 5:
#                full+=""
#                sorSzam+=1
#                sor=f.readline()
#                continue
#            if sorSzam == 8:
#                full+=""
#                sorSzam+=1
#                sor=f.readline()
#                continue
#            full+=sor
#            sorSzam+=1
#            sor=f.readline()
#        
#                
#except FileNotFoundError as fnfe:
#    print("File not found")
#    
#try:
#    with open("be.txt","w",encoding="UTF8") as f:
#            f.write(full)
#except FileNotFoundError as fnfe:
#    print("File not found")

try:
    with open("be.txt","w",encoding="UTF8") as f:
        pass # melyi ka leggyakoribb szó a fájlban?
    
except FileNotFoundError as fnfe:
    print("File not found")