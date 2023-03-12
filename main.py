###################### LİSTELER list()    #################
# listeler birden fazla veri tutmamızı sağlar
# listeler değerleri index(indis) numaralandrma ile tutarlar.
# index ilk değere 0 sayısını ve devam eden her değere 1,2,3... numaralar verir

# isimler: list = list()  # boş liste olusturur
# print(type(isimler))
#
# isimler2: list = []  # tavsiye edilmez

############## LİSTEYE VERİ EKLEME ################
# append methodu listeye veri eklemek için kullanılır

# ad: str = "hazar"
# yas: int = 23
# maas: float = 48.651
# araba: bool = True
#
# personel: list = list()
#
# personel.append(ad)
# personel.append(yas)
# personel.append(maas)
# personel.append(araba)
# print(personel)

###### TAVSİYE EDİLMEYEN YÖNTEM ###########

# personel2: list = []
# ad: str = "hazar"
# yas: int = 23
# maas: float = 48.651
# araba: bool = True
#
# personel2 += [ad]
# personel2 += [yas]
# personel2 += [maas]
# personel2 += [araba]
# print(personel2)

# ELEMANLARA ULAŞMAK
# ad: str = "hazar"
# yas: int = 23
# maas: float = 48.651
# araba: bool = True
#
# personel: list = list()
#
# personel.append(ad)
# personel.append(yas)
# personel.append(maas)
# personel.append(araba)
# print(personel)
#
# print(personel[0])
# print(personel.__getitem__(2))  # tavsiye edilen yöntem
# print(personel)
#
# personel.append("ercan")  # listeye str ekledik sonraki sırya yazar.
# print(personel)
#
# # listedeki elemanın indis değerine ulaşmak
#
# print(personel.index("ercan"))
# print(personel.index("ercan", 2))  # arama işlemine 2. elemandan sonra başla programın daha hızlı çalışmasını sağlar.

# İÇERİDEKİ BİR DEĞERİN KAÇ KERE TEKRAR ETTİĞİNİ TESPİT ETME
# count komutu

# sayilar = [10, 10, 20, 20, 30, 30, 50, 50, 50]
# print(sayilar.count(50))
# print(sayilar.count(30))
# print(sayilar.count(20))
# print(sayilar.count(10))
#
# # LİSTENİN UZUNLUĞUNU BULMA
# print(len(sayilar))
# for sayi in range(len(sayilar)):
#     print(sayilar.__getitem__(sayi))
#     print(sayilar[sayi])

# listedeki elemanları tek tek yazdırma

# for sayi in sayilar:
#     print(sayilar)
# for deger in personel:
#     print(deger)

############ ÖZEL YONTEM   ###############

# liste = [1, "elma", 3, 4, 5, True, 7, 8, 9, 10]
# print(liste[-1])  # listedeki son elemana erişmek (tersten)
# print(liste[0:4])  # 0'dan basla 4. elemana kadar git fakat 4. elemanı alma
#
# ad = "hazar"
# for harf in ad:
#     print(harf)
#
# print(ad[0:3])
# print(ad[2:])
# print(ad[:-3])

######### LİSTE SIRALAMA ##########

# liste = [1, 9, 8, 3, 99, 12]
# liste.sort()  # kucukten buyuge str'de a dan z ye
# print(liste)
#
# liste.sort(reverse=True)  # buyukten kucuge str'de z den a ya
# print(liste)


import locale
locale.setlocale(locale.LC_ALL, "tr_TR.UTF-8")  # PYTHON DİLİ TURKCE AYARLANIYOR

# sehirler = list()
# sehirler.append("ZONGULDAK")
# sehirler.append("MUĞLA")
# sehirler.append("ADANA")
# sehirler.append("MALATYA")
# sehirler.append("DÜZCE")
# sehirler.append("SİVAS")
# sehirler.append("İZMİR")
# sehirler.append("ŞANLIURFA")
# sehirler.append("KAHRAMANMARAŞ")
#
# sehirler.sort(key=locale.strxfrm)
# print(sehirler)
#
# # LİSTEDEN DEĞERLERİ DIŞARI ATMA
# sehirler.pop()  # listedeki son elemanı siler
# print(sehirler)
# sehirler.pop(2)
# print(sehirler)
#
# sehirler.remove("DÜZCE")  # LİSTEDEKİ DEĞERE GÖRE SİLER!
# print(sehirler)

# İSTENİLEN DEĞER İÇİNDE VAR MI?

# if "MALATYA" in sehirler:
#     print("malatya var")
#
# # kullanıcıdan listeye isim atamasını isteyelim ama tejrar eden değer içermesin.
# # hayır diyene kadar eklemeye devam etsin
#
# liste: list = list()
# while True:
#     cevap = input("listeye eleman eklemek için yazın ya da çıkmak için Ç basın").upper()
#
#     if cevap == "Ç":
#         break
#     else:
#         if cevap not in liste:
#             liste.append(cevap)
# for eleman in liste:
#     print(eleman)

# LİSTE BİRLEŞTİRME

# birinci_yontem_bos_liste: list = list()
# ikinci_yontem_bos_liste: list = list()
#
# a: list = [0, 1, 2, 3]
# b: list = [4, 5, 6, 7]
#
# # 1. yöntem
# birinci_yontem_bos_liste = a + b
# print(birinci_yontem_bos_liste)
#
# # 2. yöntem
# for eleman in a:
#     ikinci_yontem_bos_liste.append(eleman)
# for eleman in b:
#     ikinci_yontem_bos_liste.append(eleman)
# print(ikinci_yontem_bos_liste)

# a: list = [0, 1, 3, 2]
# referans = 0
#
# for sayi in a:
#     if sayi > referans:   # max değerdeki sayıyı yazdırır
#         referans = sayi
# print(referans)
#
# print(min(a))
# print(max(a))

# TEK SATIRDA FOR YAZMA İŞLEMİ

# sayi_listesi: list = list()
# for sayi in range(1, 11):
#     sayi_listesi.append(sayi)
# print(sayi_listesi)
#
# sayi_listesi_2 = [sayi for sayi in range(1, 11)]  # kısayol
# print(sayi_listesi_2)

# SORU 10 ile 100 arasındaki çift sayıları bir listeye atın.

# sayi_listesi = [sayi for sayi in range(10, 101, 2)]
# print(sayi_listesi)



# liste = [44, 33, 55, 66]     # adres kadıkoy
# liste2 = liste  # adres kadıkoy
# print(liste)
# print(liste2)
# liste.append(88)
# print(liste)
# print(liste2)



# a = [1, 2, 3] # ram adresi kadıkoy
# b = a.copy()  # ram adresi mecidiyekoy
#
# print(a)
# print(b)
# b.append(4)
# print(a)
# print(b)




# SORU: Kullanicidan 10 adet sayı alıp listeye atın
# ve sonrasında listenin aritmetik ortalamasını bulun.
"""
liste: list = list()
sayilar_toplami = 0
while True:
    sayi = input("Listeye sayı eklemek için yazın yazdıktan sonra ÇIK yazın:").upper()

    if sayi == "ÇIK":
        break
    else:
        if sayi not in liste:
            liste.append(sayi)
            
print(liste)
"""








# 1. 1-100 arasında 20 adet rastgele sayı üretin ve
# aynı numara içerde olmadan listeye atın.








# SORU: Klavyeden alınan 5 kelimeyi bir listeye atın.
# : Girilen 6. kelimenin listede olup olmadığını ekrana yazdırınız.

"""
import locale
locale.setlocale(locale.LC_ALL, "tr_TR.UTF-8")  # Python  dili Türkçe ayarlanıyor

liste: list = list()

while True:
    cevap = input("kelime giriniz ya da ÇIK yazınız").upper()
    if cevap == "ÇIK":
        break
    else:
        liste.append(cevap)
"""













