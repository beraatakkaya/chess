def sayilari_yazdir(sayi, dahil=False):
    if dahil:
        sayi = sayi + 1
    for i in range(sayi):
        print(i)


sayilari_yazdir(9, True)