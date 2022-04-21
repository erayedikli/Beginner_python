
import time


print("YAKIT HESAPLAYICISI BAŞLATILIYOR :")
time.sleep(2)
print('\n')

yakıt=float(input(" LÜTFEN ARACINIZIN KİLOMETRE BAŞINA YAKTIĞI YAKIT TUTARI GİRİNİZ ? :"))
yol=int(input("GİDECEĞİNİZ YOLUN KİLOMETRE CİNSİNDEN YAZINIZ ? : "))

print("TOPLAM YAKIT TUTARINIZ: ",int(yakıt*yol))
