print("""***********************
Faktöriyel Bulma Programı

-Çıkmak için q'ya basınız.

***********************""")


while True:
    sayi = input("Sayı: ")
    if (sayi == "q"):
        print("Programdan Çıkıldı.")
        break

    else:
        sayi = int(sayi)

        faktoriyel = 1

        for i in range(2,sayi+1):
            print("Faktöriyel", faktoriyel, "i:",i)
            faktoriyel *= i
        print("Faktöriyel ",faktoriyel)
