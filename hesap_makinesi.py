print("""********************
Hesap Makinesi Programı
İşlemler;

1. Toplama İşlemi
2. Çıkarma İşlemi
3. Çarpma İşlemi
4. Bölme İşlemi
********************""")

sayi1 = int(input("1. Sayıyı Girin: "))
sayi2 = int(input("2. Sayıyı Girin: "))
a = input("Yapmak İstediğiniz İşlemi Seçin: ")

if (a == "1"):
    print("Toplama İşleminin Sonucu :",(sayi1 + sayi2))
elif(a == "2"):
    print("Çıkarma İşleminin Sonucu :",(sayi1 - sayi2))
elif(a == "3"):
    print("Çarpma İşleminin Sonucu :",(sayi1 * sayi2))
elif(a == "4"):
    print("Bölme İşleminin Sonucu :",(sayi1 / sayi2))
else:
    print("Geçersiz İşlem!")

