import random
import time
start_time = time.time()

def bubble_sort(Dizi):
    for i in range(len(Dizi)-1,1,-1):
        for j in range(i) :
            if (Dizi[j] > Dizi[j+1]):
                Dizi[j] , Dizi[j+1] = Dizi[j+1] , Dizi[j]

sayi = int(input("Eleman sayisi : "))
liste = list(range(sayi))

for i in liste:
    liste[i] = random.randrange(0,100)
    print("%s. indis : "%(i),liste[i])

bubble_sort(liste)
print("\nBubble Sort ;")

for i in range(len(liste)):
    print("%s. indis : "%(i),liste[i])

print("\nKoşma Süresi : %s saniye" % (time.time() - start_time))
