#Írjunk egy olyan kódot, amely megszámolja hány darab különböző betű szerepel egy konzolról bekért mondatban,
# majd írassuk ki fordítva az egész mondatot, végül Tegyük a szavakat egy listába. 

mondat=str("")
dict= {}

print("Adj meg egy mondatot")
mondat=str(input())

for i in range(len(mondat)):
    if(mondat[i] in dict):
        dict[mondat[i]]=dict[mondat[i]]+1 # if in dict, add one to value
    else:
        dict[mondat[i]]=1                   #if not in dict, add into dict, including space(technically also a character)

toPrint=str("Betűk gyakorisága: {}")    # string that we will print ever time.
print(toPrint.format(dict)) #Print frequency
list = mondat.split(" ")
toPrint=("Fordítva: {}")    #print reverse
print(toPrint.format(mondat[::-1]))
toPrint=str("Listába rendezve szavanként: {}")
print(toPrint.format(list[::1])) # print list of words
#done