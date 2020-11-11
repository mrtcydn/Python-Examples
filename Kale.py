from random import choice

harfler=["a","b","c","d"]
x=4

tahta = []
dizi = []

for i in harfler:
    for j in range(1,x+1):
        ar = [i,j]
        tahta.append(ar)

kaleler = []
for k in range(1,x+1):
    r = choice(tahta) ; kaleler.append(r)
    print("random yerlesim : " , r)

    bas = r[0]; son = r[1]
    for t in list(tahta):
        if t[0] == bas :
            print("Yatay elenen kesisim karesi :", t);
            tahta.remove(t)
        if t[1]==son:
            print("Dikey elenen kesisim karesi :",t)
            try : tahta.remove(t)
            except: pass
print("\n\n Birbirini Yemeyen Kale yerlesimleri:\n", kaleler, "\n\n")