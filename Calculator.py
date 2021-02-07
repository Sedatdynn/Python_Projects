import math

toplama = lambda x, y: x + y

cikarma = lambda x, y: x - y

carpma = lambda x, y: x * y

bolme = lambda x, y: x // y

ust_hesap = lambda x, y: x ** y

kare_kok = lambda x: x ** 0.5

yuzde_hesap = lambda x, y: x * y // 100

cosinus = lambda x: math.sin(x)

sinus = lambda y: math.cos(y)

on_uzeri = lambda x: 10 ** x

faktoriyel = lambda n: 1 if n == 0 else n * faktoriyel(n - 1)

logaritma = lambda y, x: math.log(y, x)

cotan = lambda x: math.cos(x) / math.sin(x)


def hesapla(sec):
    if sec == "1":
        print("Sonuç: ", toplama(x, y))

    elif sec == "2":
        print("Sonuç: ", cikarma(x, y))

    elif sec == "3":
        print("Sonuç: ", carpma(x, y))

    elif sec == "4":
        print("Sonuç: ", bolme(x, y))

    elif sec == "5":
        print(f"{x} üssü {y}: ", ust_hesap(x, y))

    elif sec == "6":
        print(f"{x} sayısının kare kökü: ", round(kare_kok(x), 3))

    elif sec == "7":
        print(f"{x} sayısının yüzde {y}: ", yuzde_hesap(x, y))

    elif sec == "8":

        print(f"cosinüs{x}", cosinus(x))

    elif sec == "9":
        print(f"sinüs{y}", sinus(y))

    elif sec == "10":
        print(f"10 üzeri {x} = ", on_uzeri(x))

    elif sec == "11":
        print(f"{n} sayısının faktoriyeli = ", faktoriyel(n))

    elif sec == "12":
        print(f"{y} tabanlı logaritmanın {x} değeri =", (logaritma(x, y)))

    elif sec == "13":
        print(f"cotanjant{x} = ", cotan(x))

    elif sec =="E" or sec =="e":
        print("Çıkış yapılıyor...")



    else:
        print("İşlem aralığı 1 - 12 arasıdır!")
        sec = input("Lütfen tekrar bir işlem seçin: ")
        hesapla(sec)


lst = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13","E","e"]

while True:

    print(
        "1 - Toplama, 2 - Çıkarma , 3 - Çarpma, 4 - Bölme, 5 - Karesi, 6 - Karekök, 7 - Yüzde Hesaplama, 8 - Cos. , 9 - Sin. , 10 - 10**x , 11 - Faktoriyel, 12 - Logaritma, 13 - Cotanjant, E/e-Çıkış")
    sec = input("Lütfen bir işlem seçin: ")

    if sec not in lst:
        print("Yanlış aralık girdiniz!")
    else:

        if sec == "6":
            x = int(input("Lütfen bir sayı giriniz: "))

        elif sec == "8":
            x = int(input("Lütfen bir sayı  giriniz: "))

        elif sec == "9":
            y = int(input("Lütfen bir sayı giriniz: "))

        elif sec == "10":
            x = int(input("Lütfen bir sayı giriniz: "))

        elif sec == "11":
            n = int(input("Lütfen bir sayı giriniz: "))

        elif sec == "12":
            y = int(input("Logaritma tabanını giriniz: "))
            x = int(input("Logaritmanın sayısal değerini giriniz: "))

        elif sec == "13":
            x = int(input("Lütfen bir sayı giriniz: "))
        elif sec == "E" or sec == "e":
            print("Çıkış yapılıyor...")
            break
        else:
            x = int(input("Lütfen bir sayı giriniz: "))
            y = int(input("Lütfen bir sayı giriniz: "))

        hesapla(sec)