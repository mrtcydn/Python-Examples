import random
import time

başlangıç_zamanı = time.time()

def shaker_sort(Dizi):
    MaxYer=len(Dizi)
    MinYer=1
    while True:
        Degisti = False
        for i in range(MinYer,MaxYer):
            if(Dizi[i] < Dizi[i-1]):
                Dizi[i] , Dizi[i-1] = Dizi[i-1] , Dizi[i]
                Degisti = True
        MaxYer-=1
        if not Degisti:
            break
        i = MaxYer
        while i >= MinYer:
            if(Dizi[i] < Dizi[i-1]):
                Dizi[i] , Dizi[i-1] = Dizi[i-1] , Dizi[i]
                Degisti = True
            i-=1
        MinYer+=1
        if not(Degisti):
            break

sayi = int(input("Eleman sayisi : "))
liste = list(range(sayi))

for i in liste:
    liste[i] = random.randrange(0,100)
    print("%s. indis : "%(i),liste[i])

shaker_sort(liste)
print("\nShaker Sort ;")

for i in range(len(liste)):
    print("%s. indis : "%(i),liste[i])

print("\nKoşma Süresi : %s saniye" % (time.time() - başlangıç_zamanı))