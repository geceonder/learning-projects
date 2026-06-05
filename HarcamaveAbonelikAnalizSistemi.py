#KİŞİ BİLGİLERİ

ad = "Murat" 
soyad = "Önder"
yas = 46
sehir="İstanbul"

print("="*60)
print("  MURAT ÖNDER - Aylık Bütçe Raporu ")
print("="*60)
print("\nKişi Bilgileri:")
print(f" Ad Soyad : {ad},{soyad}")
print(f"Yaş: {yas}")
print(f"Şehir: {sehir}")


#GELİRLER

aylik_gelir = {
    "Maaş": 34000,
    "Freelance": 8500,
    "Yatirim_getirisi": 3400
    
}

print("\nGelir Bilgileri:")
print(f"Maaş   : {aylik_gelir['Maaş']} TL")
print(f"Freelance   : {aylik_gelir['Freelance']} TL")
print(f"Yatırım Getirisi  : {aylik_gelir['Yatirim_getirisi']} TL")

toplam_gelir = (
    aylik_gelir["Maaş"]+
    aylik_gelir["Freelance"]+
    aylik_gelir["Yatirim_getirisi"]
)

#GİDERLER

sabit_giderler = (
    ("kira", 18000),
    ("elektrik", 525),
    ("su", 250),
    ("doğalgaz", 650),
    ("internet", 900),
    ("ulaşım", 600),
)


toplam_sabit =(
  sabit_giderler[0][1] +
     sabit_giderler[1][1] +
     sabit_giderler[2][1] +
     sabit_giderler[3][1] +
     sabit_giderler[4][1] +
     sabit_giderler[5][1]  
)

print("\nSabit Giderler:")
print(f"Kira      : {sabit_giderler[0][1]} TL")
print(f"Elektrik  : {sabit_giderler[1][1]} TL")
print(f"Su        : {sabit_giderler[2][1]} TL")
print(f"Doğalgaz  : {sabit_giderler[3][1]} TL")
print(f"İnternet  : {sabit_giderler[4][1]} TL")
print(f"Ulaşım    : {sabit_giderler[5][1]} TL")
 
 
 
abonelikler = {
    "Netflix":          [189.90, "Eğlence"],
    "Spotify":          [ 59.99, "Müzik"],
    "YouTube Premium":  [ 79.99, "Eğlence"],
    "iCloud 50 GB":     [ 14.99, "Depolama"],
}

toplam_abonelik = (
    abonelikler["Netflix"][0]
    + abonelikler["Spotify"][0]
    + abonelikler["YouTube Premium"][0]
    + abonelikler["iCloud 50 GB"][0]
)

print("\nAbonelik Giderleri:")
print(f"Netflix          : {abonelikler['Netflix'][0]} TL")
print(f"Spotify          : {abonelikler['Spotify'][0]} TL")
print(f"YouTube Premium  : {abonelikler['YouTube Premium'][0]} TL")
print(f"iCloud           : {abonelikler['iCloud 50 GB'][0]} TL")


alisverisler = [
    ["Market",      "Haftalık market alışverişi × 4",  2400.0],
    ["Kafe/Restoran","Dışarıda yemek × 8",              1600.0],
    ["Kitap",       "3 adet kitap",                       285.0],
    ["Kıyafet",     "Spor ayakkabı",                      750.0],
    ["Sağlık",      "Vitamin takviyesi",                  320.0],
]

toplam_alisveris = (
    alisverisler[0][2]
    + alisverisler[1][2]
    + alisverisler[2][2]
    + alisverisler[3][2]
    + alisverisler[4][2]
)

print("\nAlışveriş Giderleri:")
print(f"Market         : {alisverisler[0][2]} TL")
print(f"Kafe/Restoran  : {alisverisler[1][2]} TL")
print(f"Kitap          : {alisverisler[2][2]} TL")
print(f"Kıyafet        : {alisverisler[3][2]} TL")
print(f"Sağlık         : {alisverisler[4][2]} TL")

kategoriler = {
    alisverisler[0][0],
    alisverisler[1][0],
    alisverisler[2][0],
    alisverisler[3][0],
    alisverisler[4][0],
}

toplam_gider = toplam_sabit + toplam_abonelik + toplam_alisveris
kalan_para = toplam_gelir - toplam_gider
tasarruf_orani = (kalan_para / toplam_gelir) * 100

baslik = " aylık bütçe raporu ".upper().strip()

rapor = f"""

==============================
{baslik}
==============================

Toplam Gelir        : {toplam_gelir:.2f} TL
Toplam Sabit Gider  : {toplam_sabit:.2f} TL
Abonelik Gideri     : {toplam_abonelik:.2f} TL
Alışveriş Gideri    : {toplam_alisveris:.2f} TL

TOPLAM GİDER        : {toplam_gider:.2f} TL
AY SONU KALAN       : {kalan_para:.2f} TL
Tasarruf Oranı      : %{tasarruf_orani:.2f}

Alışveriş Kategorileri:
{kategoriler}

==============================
"""

print(rapor)

