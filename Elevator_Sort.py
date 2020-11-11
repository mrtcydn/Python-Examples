import random
import time

başlangıç_zamanı = time.time()
def elevator_sort(Dizi):
    Alt = 0
    while True:
        if (Dizi[Alt] > Dizi[Alt + 1]):
            Dizi[Alt] , Dizi[Alt+1] = Dizi[Alt+1] , Dizi[Alt]
            if(Alt > 0):
                Alt-=1
        else:
            Alt+=1
        if (Alt >= (len(Dizi)-1)):
            break

sayi = int(input("Eleman sayisi : "))
liste = list(range(sayi))

for i in liste:
    liste[i] = random.randrange(0,100)
    print("%s. indis : "%(i),liste[i])

elevator_sort(liste)
print("\nElevator Sort ;")

for i in range(len(liste)):
    print("%s. indis : "%(i),liste[i])

print("\nKoşma Süresi : %s saniye" % (time.time() - başlangıç_zamanı))