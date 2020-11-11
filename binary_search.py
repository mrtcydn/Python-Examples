def binary_search(liste,aranan):
    uzunluk = len(liste)
    kucuk_indis = 0
    buyuk_indis = uzunluk-1
    while kucuk_indis <= buyuk_indis:
        orta_indis = int(( kucuk_indis + buyuk_indis ) /2)
        if( aranan == liste[orta_indis]):
            return orta_indis
        elif( aranan > liste[orta_indis]):
            kucuk_indis = orta_indis + 1
        elif( aranan < liste[orta_indis]):
            buyuk_indis = orta_indis - 1
    return -1

liste = [1,5,7,14,25,36,47,58,69,78,98]

aranan_sayi = int(input("Aramak istenilen sayi : "))

bulundu = binary_search(liste,aranan_sayi)

if bulundu >= 0:
    print("Aranan değer %s. indiste bulundu..."%(bulundu))
else:
    print("Aranan değer bulunamadı...")
