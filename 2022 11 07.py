file = open("be.txt","r",encoding="UTF8" )

tartalom = file.readlines()

for sor in tartalom:
    sor=sor.rstrip()
    print(sor)
    
file.close