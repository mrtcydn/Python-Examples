import random
import time

başlangıç_zamanı = time.time()

def straight_ınsertion_sort(Dizi):
    for i in range(1,len(Dizi)):
        T = Dizi[i]
        j=i
        while( j > 0 and Dizi[j-1] > T):
            Dizi[j] = Dizi[j-1]
            j-=1
        Dizi[j] = T

sayi = int(input("Eleman sayisi : "))
liste = list(range(sayi))

for i in liste:
    liste[i] = random.randrange(0,100)
    print("%s. indis : "%(i),liste[i])

straight_ınsertion_sort(liste)
print("\nStraight Insertion Sort ;")

for i in range(len(liste)):
    print("%s. indis : "%(i),liste[i])

print("\nKoşma Süresi : %s saniye" % (time.time() - başlangıç_zamanı))
