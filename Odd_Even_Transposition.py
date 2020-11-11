import random
import time

başlangıç_zamanı = time.time()
def odd_even_transposition(Dizi):
    for i in range(int(len(Dizi)/2)+1):
        j=0
        while (j+1 < len(Dizi)):
            if Dizi[j] > Dizi[j + 1]:
                Dizi[j], Dizi[j+1] = Dizi[j+1], Dizi[j]
            j += 2
        j=1
        while(j+1 < len(Dizi)):
             if (Dizi[j] > Dizi[j+1]):
                    Dizi[j], Dizi[j + 1] = Dizi[j + 1], Dizi[j]
             j += 2

sayi = int(input("Eleman sayisi : "))
liste = list(range(sayi))

for i in liste:
    liste[i] = random.randrange(0,100)
    print("%s. indis : "%(i),liste[i])

odd_even_transposition(liste)
print("\nOdd-Even Transposition ;")

for i in range(len(liste)):
    print("%s. indis : "%(i),liste[i])

print("\nKoşma Süresi : %s saniye" % (time.time() - başlangıç_zamanı))