import random
import time

başlangıç_zamanı = time.time()
def shaker2_sort(Dizi):
    n = len(Dizi)//2
    while n > 0:
        m=n
        while m > 0:
            for i in range((len(Dizi)-m)):
                if (Dizi[i] > Dizi[i+m]):
                    Dizi[i] , Dizi[i+m] = Dizi[i+m] , Dizi[i]
            m//=2
        n//=2
    while True:
        Degisti = False
        for j in range(len(Dizi)-1):
            if (Dizi[j] > Dizi[j+1]):
                Dizi[j] , Dizi[j+1] = Dizi[j+1] , Dizi[j]
                Degisti = True
        if not Degisti:
            break

sayi = int(input("Eleman sayisi : "))
liste = list(range(sayi))

for i in liste:
    liste[i] = random.randrange(0,100)
    print("%s. indis : "%(i),liste[i])

shaker2_sort(liste)
print("\nShaker2 Sort ;")

for i in range(len(liste)):
    print("%s. indis : "%(i),liste[i])

print("\nKoşma Süresi : %s saniye" % (time.time() - başlangıç_zamanı))