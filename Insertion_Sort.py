import random
import time

başlangıç_zamanı = time.time()

def insertion_sort(Dizi):
    for i in range(1,len(Dizi)):
        for j in range(i,0,-1):
            if Dizi[j] < Dizi[j - 1]:
                Dizi[j] , Dizi[j-1] = Dizi[j-1] , Dizi[j]
            else:
                break

sayi = int(input("Eleman sayisi : "))
liste = list(range(sayi))

for i in liste:
    liste[i] = random.randrange(0,100)
    print("%s. indis : "%(i),liste[i])

insertion_sort(liste)
print("\nInsertion Sort ;")

for i in range(len(liste)):
    print("%s. indis : "%(i),liste[i])

print("\nKoşma Süresi : %s saniye" % (time.time() - başlangıç_zamanı))
