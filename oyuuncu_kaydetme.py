print(" OYUNCU KAYDETME PROGRAMI ")
import time
ad=input("Oyuncunun Adını Giriniz: ")
soyad=input("Oyuncunun Soyadını Giriniz: ")
takım=input("Oyuncunun Oynadığı takımı Giriniz: ")

bilgiler=[ad,soyad,takım]

print("cevaplarınız işLeniyor lütfen ekranı kapatmayınız...")
time.sleep(2)
print("OYUNCU ADI: {}\nOYUNCU SOYADI: {}\nOYUNCUNUN MEVCUT TAKIMI: {} \n".format(bilgiler[0],bilgiler[1],bilgiler[2]))

print("OYUNCU BİLGİLERİ OLUŞTURULDU")