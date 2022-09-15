#Írjunk egy olyan kódot, amely megszámolja hány darab különböző betű szerepel egy konzolról bekért mondatban,
# majd írassuk ki fordítva az egész mondatot, végül Tegyük a szavakat egy listába. 

mondat=str("")
dict= {}

print("Adj meg egy mondatot")
mondat=str(input())

for i in range(len(mondat)):
    if(mondat[i] in dict):
        dict[mondat[i]]=dict[mondat[i]]+1
    else:
        dict[mondat[i]]=1
    
print("Betuk gyakorisaga: "+(dict))
list = mondat.split(" ")
print("forditva: "+list[len(list)-1])
print("Listában, szavanként:" + list[0,len(list)])





