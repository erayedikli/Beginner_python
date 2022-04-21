print("""**********************************************
*        Hesap Makinesi Programı             *
*                                            *
*            İşlem seçiniz ;                 *
*                                            *
*          1) Toplama işLemi                 *
*          2) Çıkarma işlemi                 *
*          3) Çarpma  işlemi                 *
*          4) Bölme   işlemi                 *
*                                            * 
**********************************************
""")

a=int(input("Birinci Sayıyı Giriniz :"))
b=int(input("İkinci Sayıyı Giriniz :"))
islem=input("YAPMAK İSTEDİĞNİZ İŞLEMİ GİRİNİZ:")

if (islem== "1"):
    print("{} ile {}'in TOPLAMI{}'dir. ".format(a,b,a+b))
elif (islem == "2"):
    print("{} ile {}'in FARKI {}'dir. ".format(a, b, a - b))
elif (islem== "3"):
    print("{} ile {}'in ÇARPIMI {}'dir. ".format(a,b,a*b))
elif (islem == "4"):
     print("{} ile {}'in BÖLÜMÜ {}'dir. ".format(a, b, a / b))
else:
    print("LÜTFEN GEÇERLİ BİR İŞLEM GİRİNİZ :( ......")


