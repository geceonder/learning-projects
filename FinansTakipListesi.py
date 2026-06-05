# KİŞİSEL FİNANS TAKİP SİSTEMİ

gelirler =[]
giderler =[] 

def menu_goster():
    print("\n=====================================")
    print(" FİNANS TAKİP SİSTEMİ ")
    print("\n=====================================")
    print("1) Gelir ekle")
    print("2) Gider ekle")
    print("3) Gelirleri listele")
    print("4) Giderleri listele")
    print("5) Finans Özeti")
    print("6) Çıkış")
    
def gelir_ekle():
    print(" GELİR EKLE ")
    aciklama =input("Gelir açıklaması:")
    
    tutar = float(input("Tutar (TL):"))
    if tutar < 0:
        print("Hata: Tutar negatif olamaz.")
        return
    
    kategori = input("Katagori :")
    
    kayit ={
        "aciklama":aciklama,
        "tutar":tutar,
        "kategori":kategori
    }
    gelirler.append(kayit)
    print("Gelir başarıyla eklendi.")
    
def gider_ekle():
    print(" GİDER EKLE ")
    aciklama = input("Gider açıklaması:")
    
    tutar = float(input("Tutar (TL):"))
    if tutar < 0:
        print("Hata : Tutar negatif olmaz")
        return
    
    kategori = input("Kategori:")
    
    kayit = {
        "aciklama":aciklama,
        "tutar":tutar,
        "kategori":kategori
    }
    giderler.append(kayit)
    print("Giderler başarıyla eklendi.")
    
def gelirleri_listele():
    print("--GELİR LİSTESİ--")
    if len(giderler)==0:
        print("Henüz gelir eklenmemiş.")
        return
    
    for i in range(len(gelirler)):
        kayit = gelirler [i]
        print(f"{i+1}.{kayit['aciklama']} - {kayit['tutar']}TL - {kayit['kategori']}")
        

def finans_ozeti():
    print("  FİNANS ÖZETİ  ")
    
    
toplam_gelir = 0                               #toplam gelir hesaplama
for kayit in gelirler:
    toplam_gelir = toplam_gelir + kayit["tutar"]
    
toplam_gider = 0                               #toplam gider hesaplama
for kayit in giderler:
    toplam_gider = toplam_gider + kayit["tutar"]
    
bakiye = toplam_gelir - toplam_gider         #kalan bakiye hesaplama


if bakiye > 0:                                                                #finansal yorum
    print("Yorum: Finansal durmunuz iyi ")
elif bakiye == 0 :
    print("Yorum:Gelir ve giderleriniz tam dengede")
else:
    print("Yorum: Dikkat ! Giderleriniz gelirinizden fazla")
    
if len(giderler) == 0:
     print("Henüz gider eklenmediği için kategori analizi yapılamıyor.")     #en çok harcama yapılan kategori
     
kategori_toplamlari = {}
 
for kayit in giderler:
        kategori = kayit["kategori"]
        tutar = kayit["tutar"]
 
        if kategori in kategori_toplamlari:
            kategori_toplamlari[kategori] = kategori_toplamlari[kategori] + tutar
        else:
            kategori_toplamlari[kategori] = tutar
 
en_cok_kategori = ""
en_cok_tutar = 0
 
for kategori in kategori_toplamlari:
    if kategori_toplamlari[kategori] > en_cok_tutar:
            en_cok_tutar = kategori_toplamlari[kategori]
            en_cok_kategori = kategori
 
print(f"En çok harcama yapılan kategori: {en_cok_kategori} ({en_cok_tutar} TL)")


print("Finans Takip Sistemine Hoş Geldiniz!")
 
devam = True
 
while devam:
    menu_goster()
    secim = input("Seçiminiz: ")
 
    if secim == "1":
        gelir_ekle()
    elif secim == "2":
        gider_ekle()
    elif secim == "3":
        gelirleri_listele()
    elif secim == "4":
        giderleri_listele()
    elif secim == "5":
        finans_ozeti()
    elif secim == "6":
        print("Programdan çıkılıyor... Görüşmek üzere!")
        devam = False
    else:
        print("Geçersiz seçim. Lütfen 1-6 arasında bir değer giriniz.")
 