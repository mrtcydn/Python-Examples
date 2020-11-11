import random
import time

başlangıç_zamanı = time.time()
def selection_sort(Dizi):
    for i in range(len(Dizi)-1):
        min = i
        for j in range(i+1,len(Dizi)):
            if (Dizi[j] < Dizi[min]):
                min = j
        Dizi[min] , Dizi[i] = Dizi[i] , Dizi[min]


sayi = int(input("Eleman sayisi : "))
liste = list(range(sayi))

for i in liste:
    liste[i] = random.randrange(0,100)
    print("%s. indis : "%(i),liste[i])

selection_sort(liste)
print("\nSelection Sort ;")

for i in range(len(liste)):
    print("%s. indis : "%(i),liste[i])

print("\nKoşma Süresi : %s saniye" % (time.time() - başlangıç_zamanı))