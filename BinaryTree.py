class Dugum():
    def __init__(self, bilgi):
        self.bilgi = bilgi
        self.solcocuk = None
        self.sagcocuk = None
        self.katman = None

    def __str__(self):
        return str(self.bilgi)  # Düğüm bilgisini string olarak geri döndürür.


# Bu durum bize Dugum sınıfının verilerini kullanmamamıze olanak sağlar.
class aramaagacı(Dugum):
    # Overriding işlemi olarak adlandırabiliriz.
    def __init__(self):
        self.root = None

    # İkili arama ağacında yeni düğüm oluşturur.
    def olustur(self, deger):
        if self.root == None:
            self.root = Dugum(deger)
        else:
            current = self.root

            while (True):           # Bu durunda döngü sürekli dönsün,
                if deger < current.bilgi:
                    if current.solcocuk:
                        current = current.solcocuk
                    else:
                        current.solcocuk = Dugum(deger)
                elif deger > current.bilgi:
                    if current.sagcocuk:
                        current = current.sagcocuk
                    else:
                        current.sagcocuk = Dugum(deger)
                        break
                else:
                    break

    def eaa(self):  # Enine Arama Agacı
        self.root.katman = 0            # Root'un katmanını 0'a atar.
        dizi = [self.root]              # Dizi olustur ve root'u diziye at.
        çıktı = []
        # Root'un katmanını current'ın katmanına atar.
        current_katman = self.root.katman

        # Bu while döngüsünde alınan değerlerin hangi katmanda bulunacağı ataması yapılır.
        while len(dizi) > 0:
            current_dugum = dizi.pop(0)

            if current_dugum.katman > current_katman:
                current_katman += 1
                çıktı.append("\n")

            # çıktı dizisine current_dugum 'un bilgisini yazdır.
            çıktı.append(str(current_dugum.bilgi) + " ")

            if current_dugum.solcocuk:           # current_dugum'un sol çocuğu varsa.
                current_dugum.solcocuk.katman = current_katman + 1
                # current_dugumun sol çocuğunu dizi'ye ekle.
                dizi.append(current_dugum.solcocuk)

            if current_dugum.sagcocuk:        # Current_dugum'un sağ çocuğu varsa,
                current_dugum.sagcocuk.katman = current_katman + 1
                # current_dugumun sağ çocuğunu dizi'ye ekle.
                dizi.append(current_dugum.sagcocuk)

        # çıktı dizisinin elemanlarını ayrı ayrı göstermek yerine bir bütün olarak gösterir.
        print("".join(çıktı))

    def inorder(self, dugum):     # Sıralı veya kök ortada
        if dugum != None:
            self.inorder(dugum.solcocuk)
            print(dugum.bilgi)
            self.inorder(dugum.sagcocuk)

    def preorder(self, dugum):   # Sıralı veya kök önceli
        if dugum != None:
            print(dugum.bilgi)
            self.preorder(dugum.solcocuk)
            self.preorder(dugum.sagcocuk)

    def postorder(self, dugum):  # Sıra sonralı veya kök sonda
        if dugum != None:
            self.postorder(dugum.solcocuk)
            self.postorder(dugum.sagcocuk)
            print(dugum.bilgi)


agac = aramaagacı()
dizi = [7, 5, 1, 9, 6, 15, 21, 12]
for i in dizi:
    agac.olustur(i)     # Ağaç yapısı oluşturulur.

print('Breadth-First Traversal')
agac.eaa()
print('Inorder Traversal')
agac.inorder(agac.root)
print('Preorder Traversal')
agac.preorder(agac.root)
print('Postorder Traversal')
agac.postorder(agac.root)
