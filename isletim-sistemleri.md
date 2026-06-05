
#İŞLETİM SİSTEMİ TEMELLERİ (OS Basics)

#İşletim sistemi(Operating System - OS),kullanıcı ile bilgisayar donanımı arasında köprü görevi gören temel yazılımdır. Bilgisayarın kaynaklarını yönetir,programların çalışmasını sağlar ve kullanıcıya güvenli bir çalışma ortamı sunar. İşletim sistemlerinin çalışma mantığını anlamak için kernel,süreçler,iş parçacıkları,bellek yönetimi ve CPU zamnalama mekanizmaları gibi temel kavramların bilinmesi gerekir.

#1.Kernel Nedir?
Kernel (çekirdek),işletim sisteminin en temel ve en yetkili bileşenleridir. Donanım ile yazılımlar arasındaki iletişimi sağlar ve sistem kaynaklarını yönetir.

Kernel'in Görevleri 
- CPU kullanımını yönetmek 
- Bellek yönetimini gerçekleştirmek
- Donanım aygıtlarını kontrol etmek 
- Süreçleri çalıştırmak ve sonlandırmak
- Dosya sistemine erişimi sağlamak 

Çalışma Mantığı 
Bir uygulama donanımına doğrudan erişemez.Örneğin bir program dosya okumak istediğinde istediğini kernela iletir . Kernela gerekli işlemleri gerçekleştirerek sonucu uygulamaya döndürür.  
Uygulama -> Kernela -> Donanım 
Bu yapı sayesinde sistem güvenliği ve kaynak yönetimi sağlanır.

#2.Süreç(Process) ve İş Parçacığı(Thread) Arasındaki Fark 

#Süreç (Process)
Süreç,çalışmakta olan bir programın örneğidir. Her süreç kendini bellek alanına ve sistemine sahiptir.

ÖZELLİKLERİ
- Kendi bellek alanına sahiptir
- Diğer süreçlerden izole çalışır 
- Oluşturulması ve yönetilmesi daha maliyetlidir
Örnek: Chrome.exe , VS Code.exe , Spotify.exe 
Her biri ayrı bir süreçtir.

#İş Parçacığı (Thread)
Thread,bir süreç içerisinde çalışan en küçük yürütme birimidir.Bir süreç birden fazla thread içerebilir.

ÖZELLİKLERİ
- Aynı süreç içerisindeki thread'ler ortak belleği paylaşır
- Daha hızlı oluşturulur
- Veri paylaşımı kolaydır

Örnek:
Chrome Process
├── Thread 1 (Sekme 1)
├── Thread 2 (Sekme 2)
├── Thread 3 (Ağ İşlemleri)
└── Thread 4 (Arka Plan Görevleri)

#Process ve Thread Karşılaştırması

Özellik     	           Process                           	Thread
Bellek Kullanımı	     Ayrı Bellek	                      Ortak Bellek
Oluşturma Maliyeti	       Yüksek	                             Düşük
Veri Paylaşımı	             Zor	                             Kolay
Performans	             Daha Yavaş	                           Daha Hızlı
Çökme Durumu	      Genellikle Kendini Etkiler	         Tüm Süreci Etkileyebilir

#3.Bellek Yönetimi
Bellek yönetimi, işletim sisteminin RAM kaynaklarını süreçler arasında düzenli ve verimli şekilde paylaştırmasıdır.

Bellek Kullanımı
Her çalışan süreç belirli miktarda RAM kullanır.
Örnek:
Toplam RAM  : 16 GB
Chrome      : 4 GB
VS Code     : 2 GB
Spotify     : 500 MB
İşletim Sistemi : 3 GB
İşletim sistemi bu kaynakların çakışmadan kullanılmasını sağlar.

#Sanal Bellek (Virtual Memory)
Modern işletim sistemlerinde programlar fiziksel RAM'e doğrudan erişmez. Bunun yerine her programa sanal adres alanı sunulur.

Program -> Sanal Adres -> Fiziksel RAM 
 
Bu dönüşüm CPU içerisindeki Memory Management Unit (MMU) tarafından gerçekleştirilir.

Avantajları
- Süreçler birbirinden izole edilir
- Bellek güvenliği sağlanır
- Daha büyük bellek alanları kullanılabilir

#Sayfalama (Paging)
Bellek küçük bloklara ayrılır. Bu bloklara "page" adı verilir.
Page 1
Page 2
Page 3
Page 4
İşletim sistemi hangi sayfanın RAM'de bulunduğunu takip eder. RAM yetersiz kaldığında kullanılmayan sayfalar diskteki swap alanına taşınabilir.

#4.CPU Zamanlayıcıları (CPU Schedulers)
CPU zamanlayıcısı, hangi sürecin ne zaman ve ne kadar süre çalışacağını belirleyen mekanizmadır.
Birden fazla program aynı anda çalışıyor gibi görünse de CPU işlemleri çok hızlı şekilde sırayla yürütür.
Örnek:
P1 → P2 → P3 → P1 → P2 → P3
Bu hızlı geçişler sayesinde kullanıcı tüm uygulamaların aynı anda çalıştığını düşünür.

#Round Robin Algoritması
En yaygın CPU zamanlama algoritmalarından biridir.
Her sürece belirli bir zaman dilimi (time slice) verilir.
Örnek:
P1 (10 ms)
P2 (10 ms)
P3 (10 ms)
P1 (10 ms)

Avantajları
- Adil CPU paylaşımı sağlar.
- Çok kullanıcılı sistemlerde etkilidir.

#Priority Scheduling
Bu yöntemde süreçlere öncelik değeri atanır.
Örnek:
Ses Sürücüsü : Öncelik 10
Chrome       : Öncelik 5
Notepad      : Öncelik 2
Yüksek öncelikli süreçler CPU'yu daha sık kullanır.

#SONUÇ 
İşletim sistemi; donanım kaynaklarını yöneten, programların çalışmasını sağlayan ve 
kullanıcı ile donanım arasında iletişim kuran temel sistem yazılımıdır.
Kernel, süreçler, iş parçacıkları, bellek yönetimi ve CPU zamanlayıcıları işletim 
sistemlerinin temel yapı taşlarını oluşturur.
Bu kavramların öğrenilmesi, yazılımların bilgisayar üzerinde nasıl çalıştığını anlamak 
açısından büyük önem taşır.

Bu bilgiler sayesinde bir programın CPU üzerinde nasıl yürütüldüğü, bellekte nasıl 
yürütüldüğü, bellekte nasıl saklandığı ve işletim sistemi tarafından nasıl yönetildiği daha 
iyi anlaşılabilir.Bu nedenle işletim sistemi temelleri; sistem programlama, yazılım 
geliştirme, siber güvenlik ve bulut bilişim gibi alanların temelini oluşturmaktadır.