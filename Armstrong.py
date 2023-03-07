
sayi = int(input("Sayı: "))
basamak = str(sayi)

toplam = 0

for i in basamak:
    rakam = int(i)**len(basamak)
    toplam += rakam
if (toplam == sayi):
    print("Armstrong sayıdır.")
else:
    print("Armstrong sayı değildir.")