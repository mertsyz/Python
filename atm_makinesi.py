print("""****************************
Atm Makinesine Hoşgeldiniz.

İşlemler;
1. Bakiye Sorgulama

2. Para Yatırma

3. Para Çekme

Programdan Çıkmak İçin q'ya Basın.

****************************""")

bakiye = 1000

while True:
    islem = input("İşlemi Seçiniz: ")
    if (islem == "q"):
        print("Yine Bekleriz.")
        break
    elif (islem == "1"):
        print("Bakiyeniz: {}'tldir".format(bakiye))

    elif (islem == "2"):
        print("Kaç Miktar Yatırmak İstiyorsunuz?")
        miktar = int(input("Yatırılacak Miktar: "))
        if (miktar > 0):
            bakiye += miktar
            print("Yatırılan Miktar : {}'tl\nGüncel Bakiyeniz: {}'tldir".format(miktar,bakiye))
        else:
            print("Lütfen Geçerli Miktar Giriniz.")


    elif (islem == "3"):
        print("Güncel Bakiyeniz: ",bakiye)
        cekilcek_miktar = int(input("Çekilecek Miktar: "))
        if(bakiye < cekilcek_miktar):
            print("Böyle Bir Miktar Çekemezsiniz.")
            continue
        bakiye -= cekilcek_miktar
        print("Çekilen Miktar : {}'tldir\nGüncel Bakiyeniz: {}'tl".format(cekilcek_miktar,bakiye))


    else:
        print("Geçersiz İşlem...")