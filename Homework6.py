from encodings import normalize_encoding
import string


def palindrom(a):
    a=a.lower()
    a=(irasjel_eltavolitas(a))
    if a == a[::-1]:
        print("Palindrom")
    else:
        print("Nem Palindrom")
        
def irasjel_eltavolitas(szoveg):
        irasjel_nelkuli=""
        for karakter in szoveg:
            if (karakter not in string.punctuation) and (karakter not in " "):
                irasjel_nelkuli+=karakter
        return irasjel_nelkuli

def fix(a):
    normal=""
    for i in a:
        if i in ["ö","ő","ó"]:
            normal+="o"
            continue
        if i in ["ü","ű","ú"]:
            normal+="u"
            continue
        if i =="á":
            normal+="a"
            continue
        if i =="í":
            normal+="i"
            continue
        if i =="é":
            normal+="e"
            continue
#        if i =="sz":
#            normal+="zs"
#            continue
#        if i =="zs":
#            normal+="sz"
#            continue
        else:
            normal+=i
#        normal.replace("sc","cs")
#        normal.replace("zd","dz")
#        normal.replace("szd","dzs")
#        normal.replace("yg","gy")
#        normal.replace("yt","ty")
#        normal.replace("yl","ly")
#        normal.replace("yn","ny")
#                
    return normal
        
    
    

if __name__ == "__main__":
    elrendezes="{0:>4}{1:>4}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>4}{11:>4}{12:>4}" #I CBA to make two loops of this, so heres the lazy way

    print(elrendezes.format("   ","1","2","3","4","5","6","7","8","9","10","11","12",))
    print(elrendezes.format("  :","----","----","----","----","----","----","----","----","----","----","----","----",))
    for i in range(1,13):
            print(elrendezes.format(str(i)+":",i,i*2,i*3,i*4,i*5,i*6,i*7,i*8,i*9,i*10,i*11,i*12))
            
    palindrom(input("Add meg a vizsgálni kívánt szöveget, és megmondom, palindrom-e."))