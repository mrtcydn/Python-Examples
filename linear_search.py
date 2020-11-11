def linear_search(liste,aranan_sayi):
    for i in range(len(liste)):
        if (aranan_sayi == liste[i]):
            return i
    else:
        return -1

liste = [14,65,37,48,9,74,61]
aranan_sayi = int(input("Aramak istenilen sayi : "))

bulundu = linear_search(liste,aranan_sayi)

if bulundu >= 0:
    print("Aranılan sayi %s. indiste bulunmuştur..."%(bulundu))
else:
    print("Aranılan sayi bulunamamıştır...")
