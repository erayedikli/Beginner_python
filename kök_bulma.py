"""
2. dereceden bir bilinmeyenli denklemin köklerini bulma
Denklem : ax^2 + bx + c
Deltayı Hesaplama:  b ** 2 -  4 * a * c
Birinci Kök : (-b - delta ** 0.5) / (2*a)
İkinci Kök : (-b + delta ** 0.5) / (2*a)

"""
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

delta= b**2-4*a*c

islem1=(-b - delta ** 0.5) / (2*a)
islem2=(-b + delta ** 0.5) / (2*a)

print("BİRİNCİ KÖK: {}\nİKİNCİ KÖK: {}\n".format(islem1,islem2))