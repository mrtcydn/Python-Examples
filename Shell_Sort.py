import random
import time

başlangıç_zamanı = time.time()

def shell_sort(Dizi):
    h = 1
    while((h * 3 + 1) < len(Dizi)):
        h = 3 * h + 1
    while( h > 0):
        for i in range(h-1,len(Dizi)):
            B = Dizi[i]
            j=i
            while(j>=h and (Dizi[j-h]) > B):
                Dizi[j] = Dizi[j-h]
                j -= h
            Dizi[j] = B
        h//=3

sayi = int(input("Eleman sayisi : "))
liste = list(range(sayi))

for i in liste:
    liste[i] = random.randrange(0,100)
    print("%s. indis : "%(i),liste[i])

shell_sort(liste)
print("\nShell Sort ;")

for i in range(len(liste)):
    print("%s. indis : "%(i),liste[i])

print("\nKoşma Süresi : %s saniye" % (time.time() - başlangıç_zamanı))
