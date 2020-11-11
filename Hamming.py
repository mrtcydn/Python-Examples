def isHamming(sayi):
    if(sayi==1):
        return 1
    elif(sayi % 2== 0):
        return isHamming(sayi/2)
    elif (sayi % 3== 0):
        return isHamming (sayi/3)
    elif (sayi % 5 == 0):
        return isHamming (sayi/5)
    else:
        return 0

def hamming(sayi):
    if(sayi==1):
        return True
    hamming(sayi-1)
    if(isHamming(sayi)):
        print(sayi)

hamming(15)
