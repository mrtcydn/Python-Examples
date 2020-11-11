""" Kullanıcıdan istenilen kelimenin harfleri ile oluşturulabilecek tekrarlı kelime sayısı;
 -  Kelime yazılırken büyük , küçük harf uyumuna dikkat edilmesi gerekmektedir. """

def faktöriyel (sayi):
    if (sayi<=1):
        return 1
    else:
        return sayi*faktöriyel(sayi-1)
# Girilen metindeki harflerin sayılarını bulma
kelime = str(input("Lütfen bir kelime giriniz: "))
harf = []
sayi = []
bölen = 0
for i in (kelime):  # Girilen kelimede ki her harf için;
    if not (i in harf):  # Kontrol edilen harf harf listesinde yoksa
        harf.append(i)   # Harfi harf listesine ata,
        sayi.append(1)   # Ve sayi listesine 1 ekle.
    else:
        # Eğer harf listesinde aynı harf var ise harfe karşılık gelen sayı değerini 1 arttır.
        sayi[harf.index(i)] = sayi[harf.index(i)] + 1
for j in range(len(harf)):
    print(harf[j], " harfinden  --> %s  adet bulunmakta."%(sayi[j]))
    bölen += faktöriyel(sayi[j])

n = 0
for i in range(len(sayi)):
    # Harflerin toplam sayısı
    n += sayi[i]

sonuç = faktöriyel(n)//bölen
print("Tekrarlı permütasyon sonucu oluşturulabilecek kelime sayısı : ",sonuç)
