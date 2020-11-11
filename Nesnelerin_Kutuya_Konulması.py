""" 1 ile 99.999 arasında rakamlar toplamı 8 ve 8'den küçük sayıların miktarını belirten kod.
 -  Bulunan sayıların hepsi 5 basamaklı olarak yazılarak 1-8 arası nesnelerin
 5 kutuya yerleştirilmesi olarak yorumlanabilir.Örneğin; 231 sayısı 00231 yazılarak aslında;
 |   |   | * * | * * * | * | şeklinde düşünülenebilir. """
toplam = 0
for sayi in range(1,99999):
    rakamlar_toplamı = 0
    num = sayi
    while num > 0:
        rakamlar_toplamı+=num%10   # Sayının birler basamağı alınır.
        num = num//10    # 10'a bölme işlemi ile sayının birler basamağı atılırak  yeni sayı elde edilir.
    if rakamlar_toplamı <= 8 :
        toplam +=1    # Uygun toplam sayı miktarı.
        print("%05d" %(sayi)) # Uygun sayılar 5 basamaklı hale çeviriliyor.

print("\nRakamlar toplamı 8 ve 8'den küçük olan %s adet sayı vardır."%(toplam))