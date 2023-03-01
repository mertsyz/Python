print("""
Geometrik Şekil Hesapla

1. İşlem Üçgen Bulma
2. İşlem Dörtgen Bulma
""")

islem = input("İşlem Seçiniz: ")

if (islem == "2"):
    kenar = int(input("1. kenarın uzunluğu: "))
    kenar2 = int(input("2. kenarın uzunluğu: "))
    kenar3 = int(input("3. kenarın uzunluğu: "))
    kenar4 = int(input("4. kenarın uzunluğu: "))
    if (kenar == kenar2 == kenar3 == kenar4):
        print("Dörtgen Karedir.")
    elif (kenar == kenar2 and kenar3 == kenar4):
        print("Dörtgen Dikdörtgendir.")
    else:
        print("Sıradan Bir Dörtgen.")

elif (islem == "1"):
    ucgenkenar = int(input("1. kenarın uzunluğu: "))
    ucgenkenar1 = int(input("2. kenarın uzunluğu: "))
    ucgenkenar2 = int(input("3. kenarın uzunluğu: "))
    if(ucgenkenar == ucgenkenar1 == ucgenkenar2):
        print("Eşkenar Üçgendir.")
    elif(ucgenkenar == ucgenkenar1 or ucgenkenar1 == ucgenkenar2 or ucgenkenar == ucgenkenar2):
        print("İkizkenar Üçgendir.")
    else:
        print("Çeşit Kenar Üçgendir.")




