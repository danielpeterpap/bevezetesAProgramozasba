from encodings import normalize_encoding
import string


def palindrom(a):
    a = a.lower()
    a = fix(irasjel_eltavolitas(a))
    # print(a)
    # onovottotavakazszsirisrizsoytoladobobantisementolosuttacieregiboravakolatjelonezramzsekililezsemeldobahatosagaygakeletrekkenohirebotkoscaynegelabalozorivargabetutarauzstralvekniscikoseaberohalkanhasitelekpanelagiridikullemaradohkiselogatnaygernooidamagoroscerrenezokozsaletterokmorkajakosoktufateisajaroletetgeleleygeisomodikisamoripatakabalonahorkantobenotagutitnatitantitugatonebotnakrohanolabakatapiromasikidomosieygelelegtetelorajasietafutkosokajakromkorettelazsokozenerrescorogamadioonreygantagolesikhodaramellukidirigalenapkeletisahnaklahorebaesokiscinkevlartzsuaratutebagravirozolabalegeynascoktoberihonekkertelekaygagasotahabodlemezselilikezsmarzenolejtalokavarobigereicattusolotnemesitnabobodaloytozsirsirizssakavatottovono
    # onovottotavakasszirisriszotyoladobobantisementolosuttacieregiboravakolatjelonezramszekilileszemeldobahatosagagyakeletrekkenohirebotkocsanyegelabalozorivargabetutarausztralveknicsikoseaberohalkanhasitelekpanelagiridikullemaradohkiselogatnagyernooidamagorocserrenezokoszaletterokmorkajakosoktufateisajaroletetgelelegyeisomodikisamoripatakabalonahorkantobenotagutitnatitantitugatonebotnakrohanolabakatapiromasikidomosiegyelelegtetelorajasietafutkosokajakromkorettelaszokozenerrecsorogamadioonregyantagolesikhodaramellukidirigalenapkeletisahnaklahorebaesokicsinkevlartszuaratutebagravirozolabalegenyacsoktoberihonekkertelekagyagasotahabodlemeszelilikeszmarzenolejtalokavarobigereicattusolotnemesitnabobodalotyoszirsiriszszakavatottovono
    # print(a[::-1])

    if a == a[::-1]:
        print("Palindrom")
    else:
        print("Nem Palindrom")


def irasjel_eltavolitas(szoveg):
    irasjel_nelkuli = ""
    for karakter in szoveg:
        if (karakter not in string.punctuation) and (karakter not in " "):
            irasjel_nelkuli += karakter
    return irasjel_nelkuli


def fix(a):
    normal = ""
    for i in a:
        if i in ["ö", "ő", "ó"]:
            normal += "o"
            continue
        if i in ["ü", "ű", "ú"]:
            normal += "u"
            continue
        if i == "á":
            normal += "a"
            continue
        if i == "í":
            normal += "i"
            continue
        if i == "é":
            normal += "e"
            continue
        else:
            normal += i
#        normal.replace("sc","cs")
#        normal.replace("zd","dz")
# normal.replace("yg","gy")
#        normal.replace("yt","ty")
#        normal.replace("yl","ly")
#        normal.replace("yn","ny")
#    normal2=""
#    for i in range(len(normal)):
#        if "szd" in normal[i:i+2]:
#            i=i+2
#            normal2+="dzs"
#            continue
#        if "sz" in normal[i:i+1]:
#            i=i+1
#            normal2+="zs"
#            continue
#        if "zs" in normal[i:i+1]:
#            i=i+1
#            normal2+="sz"
#            continue
#        else:
#            normal2+=normal[i]
#
#
#
#
#
    return normal


if __name__ == "__main__":
    # I CBA to make two loops of this, so heres the lazy way
    elrendezes = "{0:>4}{1:>4}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>4}{11:>4}{12:>4}"

    print(elrendezes.format("   ", "1", "2", "3", "4",
          "5", "6", "7", "8", "9", "10", "11", "12",))
    print(elrendezes.format("  :", "----", "----", "----", "----",
          "----", "----", "----", "----", "----", "----", "----", "----",))
    for i in range(1, 13):
        print(elrendezes.format(str(i)+":", i, i*2, i*3, i *
              4, i*5, i*6, i*7, i*8, i*9, i*10, i*11, i*12))

    palindrom(
        input("Add meg a vizsgálni kívánt szöveget, és megmondom, palindrom-e."))
