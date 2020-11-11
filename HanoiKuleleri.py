def yaz():
    print("Çubuk1 : ", Cubuk1)
    print("Çubuk2 : ", Cubuk2)
    print("Çubuk3 : ", Cubuk3)

def hanoi(n  , x, y, z):
    if(n==1):
        print("Diski %s çubuğundan %s çubuğuna koy." % (x, z))
        if(x=='A' and z=='C'):
            Cubuk3.append(Cubuk1.pop())     #Cubuk1'in en üsteki elemanını alır ve Cubuk3'e ekler.
            yaz()
        elif(x=='A' and z=='B'):
            Cubuk2.append((Cubuk1.pop()))   #Cubuk1'in en üsteki elemanını alır ve Cubuk2'e ekler.
            yaz()
        elif(x=='B' and z=='A'):
            Cubuk1.append(Cubuk2.pop())     #Cubuk2'in en üsteki elemanını alır ve Cubuk1'e ekler.
            yaz()
        elif(x=='B' and z=='C'):
            Cubuk3.append(Cubuk2.pop())     #Cubuk2'in en üsteki elemanını alır ve Cubuk3'e ekler.
            yaz()
        elif(x=='C' and z=='A'):
            Cubuk1.append(Cubuk3.pop())     #Cubuk3'in en üsteki elemanını alır ve Cubuk1'e ekler.
            yaz()
        else:
            Cubuk2.append(Cubuk3.pop())
            yaz()
    else:
        hanoi(n-1,x ,z ,y)
        hanoi(1  ,x ,y ,z)
        hanoi(n-1 ,y ,x ,z)

n= int(input("Disk sayisi N : "))
Cubuk1=[]
Cubuk2=[]
Cubuk3=[]

for i in range(n,0,-1):
    Cubuk1.append(i)

yaz()

hanoi(n,'A','B','C')
