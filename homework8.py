if __name__ == '__main__':
    lista=[2,5,6,8,13,32,42,50,53,62,66,70,80,89,91]
    down, up = 0, len(lista)-1
    find=int(70)
    steps=0
    while down <= up:
        k=(down+up)//2
        if find < lista[k]:
            up=k-1
            steps+=1
        elif find > lista[k]:
            down = k+1
            steps+=1
        else:
            print(steps," lépésben találta meg a ",find," számot, az alsó értéke ",down,", a felső étéke pedig ",up,". K értéke: ",k)
            break