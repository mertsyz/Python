print("Mükemmel Sayı Bulma")

sayi = int(input("Sayı: "))

toplam = 0

for i in range(1,sayi):
    if (sayi % i ==0):
        toplam += i
if (toplam == sayi):
    print("Mükemmel Sayıdır.")
else:
    print("Mükemmel Sayı Değildir.")
