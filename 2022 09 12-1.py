x=1
y=2
print(x)
print(y)

a=float(x)
b=int(y)

print(a)
print(b)

print(type(a))
print(type(b))

################################################################

for x in "banana":
    print(x)
a="Hello world!"
print(len(a))

txt = "The best things in life are free!"

if "free" in txt:
    print("contain")
print(txt.upper())
print(txt.lower())

a= "Hello, world!"
print(a.split(' '))
a="hello "
b="world"
c=a+b
print(c)
print(a+b)

################################################################

age= 26
txt= "I am {}"
print(txt.format(age))

quantity=3
Itemno = 564
price=70.83
myorder= "I want {} pieces of {} for {}"
print(myorder.format(quantity,Itemno,price))

###################################################################
#print("adjon meg 2 egész számot!")
#a=int(input())
#b=int(input())
#if a > b:
#    print("a greater than b")
#else:
#    print("b greater than a")

###############################

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango","melon"]

print(thislist[2:5]) # 2-től 5 ig
print(thislist[:4]) # 4 ig az elejétől
print(thislist[-4:-1]) # hátulról kezd
print(thislist[::-1]) # visszafele
print(thislist[0:len(thislist):3]) # minden 3.

#thislist[1:3] = ["valami", "cica"]
#print(thislist)

#thislist.insert(2,"watermelon")
#print(thislist)

thislist.append("watermelon")
print(thislist)


