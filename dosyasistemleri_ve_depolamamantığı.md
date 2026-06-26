# Dosya Sistemleri ve Depolama Mantığı
# Giriş 

Bilgisayar sistemlerinde verilerin saklanması, düzenlenmesi ve erişilmesi için dosya 
sistemleri kullanılır. İşletim sistemleri, depolama aygıtları üzerindeki verileri yönetmek 
için farklı dosya sistemleri geliştirmiştir. Bu raporda NTFS, ext4 ve APFS dosya sistemleri incelenecek, blok yapısı açıklanacak ve HDD ile SSD depolama teknolojilerinin çalışma 
prensipleri karşılaştırılacaktır.

#1. Dosya Sistemleri

Dosya sistemi, verilerin depolama aygıtları üzerinde nasıl organize edileceğini belirleyen 
yapıdır. Bir dosyanın nerede saklandığı, nasıl erişileceği ve güvenlik izinleri gibi işlemler 
dosya sistemi tarafından yönetilir.

1.1 NTFS (New Technology File System)

NTFS, Microsoft tarafından geliştirilmiş ve Windows işletim sistemlerinde kullanılan 
varsayılan dosya sistemidir.

Özellikleri
Büyük dosya ve disk desteği sağlar.
Dosya izinleri ve erişim kontrolü sunar.
Veri sıkıştırma desteği vardır.
Şifreleme (EFS) desteği bulunur.
Journaling özelliği sayesinde veri bütünlüğünü korur.
Avantajları
Güçlü güvenlik mekanizmaları
Büyük depolama alanlarını desteklemesi
Hata toleransının yüksek olması
Dezavantajları
Linux ve macOS tarafından tam desteklenmez.
Yapısı diğer bazı dosya sistemlerine göre daha karmaşıktır.


1.2 ext4 (Fourth Extended File System)

ext4, Linux sistemlerinde en yaygın kullanılan dosya sistemidir.

Özellikleri
Yüksek performans sunar.
Journaling desteği vardır.
Büyük dosya ve bölüm desteği sağlar.
Fragmentasyonu azaltacak şekilde tasarlanmıştır.
Avantajları
Kararlı ve güvenilir yapı
Linux sistemlerinde yüksek performans
Düşük sistem kaynağı kullanımı
Dezavantajları
Windows tarafından yerel olarak desteklenmez.
APFS kadar gelişmiş snapshot özellikleri içermez.

1.3 APFS (Apple File System)

APFS, Apple tarafından macOS, iOS ve diğer Apple cihazları için geliştirilmiştir.

Özellikleri
SSD depolama için optimize edilmiştir.
Güçlü şifreleme desteği sunar.
Snapshot özelliği sayesinde sistem geri yükleme işlemlerini kolaylaştırır.
Copy-on-Write teknolojisini kullanır.
Avantajları
SSD üzerinde yüksek performans
Güçlü veri koruma mekanizmaları
Hızlı dosya kopyalama işlemleri
Dezavantajları
Apple ekosistemi dışındaki sistemlerde sınırlı destek
HDD üzerinde performansı ext4 kadar verimli olmayabilir
1.4 NTFS - ext4 - APFS Karşılaştırması
Özellik	NTFS	ext4	APFS
İşletim Sistemi	Windows	Linux	macOS/iOS
Journaling	Var	Var	Var
Şifreleme	Var	Sınırlı	Gelişmiş
SSD Optimizasyonu	Orta	İyi	Çok İyi
Snapshot	Sınırlı	Ek araçlarla	Yerleşik
Performans	İyi	Çok İyi	Çok İyi

#2. Blok Yapısı Nedir?

Dosya sistemleri verileri doğrudan byte byte depolamaz. Bunun yerine veriler blok adı verilen sabit boyutlu alanlarda tutulur.

Örneğin:

Blok boyutu: 4 KB
Dosya boyutu: 10 KB

Bu durumda dosya:


blok = 4 KB


blok = 4 KB


blok = 2 KB

şeklinde depolanır.

Blok Yapısının Avantajları
Veri yönetimini kolaylaştırır.
Okuma ve yazma işlemlerini hızlandırır.
Dosya sisteminin performansını artırır.
Basit Gösterim
Disk

[Blok 1] [Blok 2] [Blok 3] [Blok 4] [Blok 5]

Dosya A:
[Blok 1][Blok 2]

Dosya B:
[Blok 4][Blok 5]

İşletim sistemi, dosyanın hangi bloklarda bulunduğunu metadata tablolarında saklar.

#3. HDD ve SSD Çalışma Prensipleri
3.1 HDD (Hard Disk Drive)

HDD'ler mekanik yapıya sahip depolama aygıtlarıdır.

Çalışma Mantığı
Disk plakaları sürekli döner.
Okuma/yazma kafası hareket ederek veriye ulaşır.
Veri manyetik olarak saklanır.
Yapısı
     Okuma/Yazma Kafası
              |
              V
    -------------------
   /                   \
  |     Dönen Disk      |
   \___________________/
Avantajları
Düşük maliyet
Büyük depolama kapasitesi
Dezavantajları
Mekanik parçalar nedeniyle yavaş çalışma
Darbelere karşı hassas yapı
Daha yüksek enerji tüketimi
3.2 SSD (Solid State Drive)

SSD'ler hareketli parça içermeyen depolama aygıtlarıdır.

Çalışma Mantığı
Veriler NAND Flash bellek hücrelerinde saklanır.
Elektronik devreler üzerinden erişim sağlanır.
Fiziksel hareket gerektirmez.
Yapısı
CPU
 |
 V
SSD Controller
 |
 +---- NAND Flash
 +---- NAND Flash
 +---- NAND Flash
Avantajları
Çok hızlı veri erişimi
Düşük enerji tüketimi
Sessiz çalışma
Darbelere karşı dayanıklı yapı
Dezavantajları
HDD'lere göre daha pahalıdır.
Yazma ömrü sınırlıdır (günümüzde oldukça yüksektir).


#4. Veri Okuma ve Yazma Hızları Nereden Gelir?

Depolama performansını belirleyen temel faktörler şunlardır:

#HDD

HDD'de hız;

Diskin dönme hızı (RPM)
Kafanın hareket süresi (Seek Time)
Veri aktarım hızı

gibi fiziksel faktörlere bağlıdır.

Örneğin:

5400 RPM HDD
7200 RPM HDD

7200 RPM disk daha hızlı veri erişimi sağlar.

#SSD

SSD'de hız;

NAND Flash teknolojisi
SSD kontrolcüsü
PCIe veya SATA arayüzü

tarafından belirlenir.

Örnek hızlar:

Depolama Türü	Ortalama Hız
HDD	80 - 200 MB/s
SATA SSD	500 - 600 MB/s
NVMe SSD	3000 - 14000 MB/s

#Sonuç

Dosya sistemleri, depolama aygıtları üzerindeki verilerin organize edilmesini sağlar. NTFS 
Windows sistemlerinde, ext4 Linux sistemlerinde ve APFS ise Apple cihazlarında yaygın olarak 
kullanılmaktadır. Dosya sistemlerinin temel çalışma mantığı blok yapısına dayanır. Depolama 
teknolojileri açısından HDD'ler mekanik yapıları nedeniyle daha yavaş çalışırken, SSD'ler 
elektronik bellek hücreleri sayesinde çok daha hızlı veri erişimi sağlar. Günümüzde özellikle 
NVMe SSD teknolojileri, veri okuma ve yazma performansında önemli avantajlar sunmaktadır.

