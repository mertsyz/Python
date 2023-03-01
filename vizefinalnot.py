print("Vize Final Not Hesaplama")

vize1 = int(input("1. Vize Notunuzu Giriniz: "))
vize2 = int(input("2. Vize Notunuzu Giriniz: "))
final = int(input("Final Notunuzu Giriniz: "))
hesap = (vize1 * 0.3) + (vize2 * 0.3) + (final * 0.4)

if (hesap >= 90):
    print("Notunuz: {}\nHarf Notunuz: {}".format(hesap,"AA"))
elif (hesap >= 85):
    print("Notunuz: {}\nHarf Notunuz: {}".format(hesap,"BA"))
elif (hesap >= 80):
    print("Notunuz: {}\nHarf Notunuz: {}".format(hesap,"BB"))
elif (hesap >= 75):
    print("Notunuz: {}\nHarf Notunuz: {}".format(hesap,"CB"))
elif (hesap >= 70):
    print("Notunuz: {}\nHarf Notunuz: {}".format(hesap,"CC"))
elif (hesap >= 65):
    print("Notunuz: {}\nHarf Notunuz: {}".format(hesap,"DC"))
elif (hesap >= 60):
    print("Notunuz: {}\nHarf Notunuz: {}".format(hesap,"DD"))
elif (hesap >= 55):
    print("Notunuz: {}\nHarf Notunuz: {}".format(hesap,"FD"))
elif (hesap < 55):
    print("Notunuz: {}\nHarf Notunuz: {}".format(hesap,"FF"))