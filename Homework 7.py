import string

def irasjel_eltavolitas(szoveg):
    irasjel_nelkuli = ""
    for karakter in szoveg:
        if (karakter not in string.punctuation) and (karakter not in " "):
            irasjel_nelkuli += karakter
    return irasjel_nelkuli

def nncsMgnhngz(a):
    normal = ""
    for i in a:
        if i in ["ö", "ő", "ó", "o","a","á","í","i","e","é","ü", "ű", "ú","u","Ö", "Ő", "Ó","A","Á","Í","I","E","É","Ü", "Ű", "Ú","U"]:
            normal += "" #.lower() nem műlödik a magyar karakterek miatt
            continue
        else:
            normal += i
    return normal



if __name__ == '__main__':
    full=""
    try:
        with open("hazi.txt","r",encoding="UTF8") as f:
            sor=f.readline()
            i=1
            while sor:
                if sor=="\n":
                    sor=f.readline()
                    continue
                if i %3==0:
                    sor=nncsMgnhngz(irasjel_eltavolitas(sor))
                    full+=sor
                i+=1
                sor=f.readline()
    except FileNotFoundError as fnfe:
        print ("File not found")
    
    
    with open("hazi_kimenet.txt", "w") as f:
        f.write(full)
        