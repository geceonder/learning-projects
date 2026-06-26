# = AKILLI KAMPÜS ETKİNLİK VE KATILIMCI YÖNETİM SİSTEMİ =

# __ 1.SINIF : Paticipant (katılımcı)______________________

class Participant :
    """
    Bir üniversite kulübü üyesini temsil eder.
    
    Özellikler
    ----------
    name         :str - AD SOYAD
    student_no   :str - Öğrenci numarası (benzersiz anahtar)
    department   :str - Bölüm adı
    interests    :set - İlgi alanları (aynı alan tekrar eklenmez)
    joined_events:list - Katıldığı etkinliklerin başlıkları 
    
    """
    
    def __init__(self,name: str, student_no: str,department: str, interests:set):
        
        self.name=name
        self.student_no=student_no
        self.department=department
        self.interests=interests       #set
        self.joined_events:list=[]     #list
        
 # ── Bilgi görüntüleme ──────────────────────────────────
    def display_info(self) -> None:
        """Katılımcının tüm bilgilerini terminale yazar."""
        joined_str = (
            ", ".join(self.joined_events) if self.joined_events else "Henüz yok"
        )
        print(f"""
  ─ Katılımcı Bilgileri ──────────────────────────────
    Ad            : {self.name}
    Öğrenci No    : {self.student_no}
    Bölüm         : {self.department}
    İlgi Alanları : {', '.join(self.interests)}
    Katıldığı Etk.: {joined_str}
  ────────────────────────────────────────────────────""")
 
 # ── İlgi alanı ekleme ─────────────────────────────────
    def add_interest(self, interest: str) -> None:
        """Set yapısı sayesinde aynı ilgi alanı iki kez eklenmez."""
        self.interests.add(interest.strip())
 
    def __repr__(self) -> str:
        return f"<Participant {self.student_no}: {self.name}>"
 
 
# ─────────────────────────────────────────────
# 2. SINIF: Event (Etkinlik)
# ─────────────────────────────────────────────
class Event:
    """
    Bir kulüp etkinliğini temsil eder.
 
    Özellikler
    ----------
    title        : str  – Etkinlik başlığı (benzersiz anahtar)
    category     : str  – Kategori (öneri sistemi bu alanı kullanır)
    quota        : int  – Maksimum katılımcı sayısı
    participants : list – Kayıtlı öğrenci numaraları
    """
 
    def __init__(self, title: str, category: str, quota: int):
        self.title = title
        self.category = category
        self.quota = quota
        self.participants: list = []   # öğrenci numaraları tutulur
 
    # ── Doluluk kontrolü ──────────────────────────────────
    def is_full(self) -> bool:
        """Kontenjan doluysa True döner."""
        return len(self.participants) >= self.quota
 
    # ── Katılımcı ekleme ──────────────────────────────────
    def add_participant(self, student_no: str) -> None:
        """Öğrenci numarasını etkinlik listesine ekler."""
        self.participants.append(student_no)
 
    # ── Doluluk oranı ─────────────────────────────────────
    def get_occupancy_rate(self) -> float:
        """Doluluk oranını yüzde (0-100) olarak döner."""
        if self.quota == 0:
            return 0.0
        return (len(self.participants) / self.quota) * 100
 
    # ── Kalan kontenjan ───────────────────────────────────
    def remaining_quota(self) -> int:
        """Kalan kontenjan sayısını döner."""
        return self.quota - len(self.participants)
 
    # ── Özet bilgi ────────────────────────────────────────
    def display_summary(self) -> None:
        """Etkinlik özet bilgisini terminale yazar."""
        print(f"""
  ┌─ Etkinlik ─────────────────────────────────────────┐
  │  Başlık          : {self.title}
  │  Kategori        : {self.category}
  │  Kontenjan       : {self.quota}
  │  Kayıtlı Kişi   : {len(self.participants)}
  │  Kalan Kontenjan : {self.remaining_quota()}
  └────────────────────────────────────────────────────┘""")
 
    def __repr__(self) -> str:
        return f"<Event '{self.title}' ({len(self.participants)}/{self.quota})>"
 
 
# ─────────────────────────────────────────────
# 3. SINIF: ClubSystem (Yönetim Sistemi)
# ─────────────────────────────────────────────
class ClubSystem:
    """
    Tüm sistemi yöneten ana sınıf.
 
    Özellikler
    ----------
    participants : dict  – { student_no: Participant }
    events       : dict  – { title: Event }
    """
 
    def __init__(self):
        self.participants: dict = {}  # key: student_no
        self.events: dict = {}        # key: title
 
    # ══════════════════════════════════════════════════════
    # ÖZELLIK 1 – Katılımcı Ekle
    # ══════════════════════════════════════════════════════
    def add_participant(self) -> None:
        """Konsoldan bilgi alarak yeni katılımcı oluşturur."""
        print("\n── Katılımcı Ekle ──────────────────────────────────")
 
        name = input("  Ad Soyad       : ").strip()
        student_no = input("  Öğrenci No     : ").strip()
        department = input("  Bölüm          : ").strip()
        interests_raw = input("  İlgi Alanları  : (virgülle ayır) ").strip()
 
        # Giriş doğrulama
        if not name or not student_no or not department:
            print("\n  [!] Ad, öğrenci no ve bölüm alanları boş bırakılamaz.")
            return
 
        # Aynı öğrenci no var mı?
        if student_no in self.participants:
            print(f"\n  [!] '{student_no}' numaralı öğrenci zaten kayıtlı.")
            return
 
        # İlgi alanlarını set'e çevir
        interests: set = {
            item.strip()
            for item in interests_raw.split(",")
            if item.strip()
        }
 
        # Nesne oluştur ve sözlüğe ekle
        new_participant = Participant(name, student_no, department, interests)
        self.participants[student_no] = new_participant
 
        print(f"\n  [✓] '{name}' başarıyla sisteme eklendi.")
 
    # ══════════════════════════════════════════════════════
    # ÖZELLIK 2 – Etkinlik Oluştur
    # ══════════════════════════════════════════════════════
    def create_event(self) -> None:
        """Konsoldan bilgi alarak yeni etkinlik oluşturur."""
        print("\n── Etkinlik Oluştur ────────────────────────────────")
 
        title = input("  Etkinlik Adı   : ").strip()
        category = input("  Kategori       : ").strip()
        quota_str = input("  Kontenjan      : ").strip()
 
        # Giriş doğrulama
        if not title or not category:
            print("\n  [!] Etkinlik adı ve kategori boş bırakılamaz.")
            return
 
        if not quota_str.isdigit() or int(quota_str) <= 0:
            print("\n  [!] Kontenjan pozitif bir tam sayı olmalıdır.")
            return
 
        quota = int(quota_str)
 
        # Aynı isimde etkinlik var mı?
        if title in self.events:
            print(f"\n  [!] '{title}' adlı etkinlik zaten mevcut.")
            return
 
        new_event = Event(title, category, quota)
        self.events[title] = new_event
 
        print(f"\n  [✓] '{title}' etkinliği başarıyla oluşturuldu.")
 
    # ══════════════════════════════════════════════════════
    # ÖZELLIK 3 – Katılımcıyı Etkinliğe Kaydet
    # ══════════════════════════════════════════════════════
    def register_participant(self) -> None:
        """Öğrenciyi seçilen etkinliğe kayıt eder; 4 kontrol yapar."""
        print("\n── Etkinliğe Kayıt ────────────────────────────────")
 
        student_no = input("  Öğrenci No     : ").strip()
        event_title = input("  Etkinlik Adı   : ").strip()
 
        # Kontrol 1 – Öğrenci var mı?
        if student_no not in self.participants:
            print(f"\n  [!] '{student_no}' numaralı öğrenci bulunamadı.")
            return
 
        # Kontrol 2 – Etkinlik var mı?
        if event_title not in self.events:
            print(f"\n  [!] '{event_title}' adlı etkinlik bulunamadı.")
            return
 
        participant = self.participants[student_no]
        event = self.events[event_title]
 
        # Kontrol 3 – Öğrenci zaten kayıtlı mı?
        if event_title in participant.joined_events:
            print(f"\n  [!] '{participant.name}' zaten bu etkinliğe kayıtlı.")
            return
 
        # Kontrol 4 – Kontenjan dolu mu?
        if event.is_full():
            print(f"\n  [!] '{event_title}' etkinliğinin kontenjanı dolmuştur.")
            return
 
        # Her şey uygun → kayıt
        event.add_participant(student_no)
        participant.joined_events.append(event_title)
 
        print(
            f"\n  [✓] '{participant.name}' → '{event_title}' etkinliğine başarıyla kaydedildi."
        )
 
    # ══════════════════════════════════════════════════════
    # ÖZELLIK 4 – Tüm Katılımcıları Listele
    # ══════════════════════════════════════════════════════
    def list_participants(self) -> None:
        """Sistemdeki tüm katılımcıları ekrana yazdırır."""
        print("\n── Tüm Katılımcılar ────────────────────────────────")
 
        if not self.participants:
            print("  Henüz hiç katılımcı eklenmemiş.")
            return
 
        for participant in self.participants.values():
            participant.display_info()
 
        print(f"\n  Toplam katılımcı: {len(self.participants)}")
 
    # ══════════════════════════════════════════════════════
    # ÖZELLIK 5 – Tüm Etkinlikleri Listele
    # ══════════════════════════════════════════════════════
    def list_events(self) -> None:
        """Sistemdeki tüm etkinlikleri ekrana yazdırır."""
        print("\n── Tüm Etkinlikler ─────────────────────────────────")
 
        if not self.events:
            print("  Henüz hiç etkinlik oluşturulmamış.")
            return
 
        for event in self.events.values():
            event.display_summary()
 
        print(f"\n  Toplam etkinlik: {len(self.events)}")
 
    # ══════════════════════════════════════════════════════
    # ÖZELLIK 6 – Katılımcıya Etkinlik Öner
    # ══════════════════════════════════════════════════════
    def suggest_events(self) -> None:
        """
        Katılımcının ilgi alanları ile etkinlik kategorisini karşılaştırır.
        Zaten katılındı veya kontenjanı dolu etkinlikler önerilmez.
        """
        print("\n── Etkinlik Önerisi ────────────────────────────────")
 
        student_no = input("  Öğrenci No : ").strip()
 
        if student_no not in self.participants:
            print(f"\n  [!] '{student_no}' numaralı öğrenci bulunamadı.")
            return
 
        participant = self.participants[student_no]
 
        # Etkinlik listesi boş mu?
        if not self.events:
            print("\n  Henüz hiç etkinlik oluşturulmamış.")
            return
 
        suggested: list = []
 
        for event in self.events.values():
            # Öneri koşulları:
            already_joined = event.title in participant.joined_events
            category_match = event.category in participant.interests
            has_quota = not event.is_full()
 
            if category_match and not already_joined and has_quota:
                suggested.append(event)
 
        print(f"\n  Katılımcı : {participant.name}")
        print(f"  İlgi Alan.: {', '.join(participant.interests)}\n")
 
        if suggested:
            print("  Önerilen Etkinlikler:")
            for ev in suggested:
                # tuple ile birlikte başlık ve kalan kontenjan göster
                info_tuple = (ev.title, ev.category, ev.remaining_quota())
                print(
                    f"    - {info_tuple[0]}  |  Kategori: {info_tuple[1]}"
                    f"  |  Kalan Kont.: {info_tuple[2]}"
                )
        else:
            print("  Uygun öneri bulunamadı.")
            print("  (Tüm uygun etkinliklere kayıtlı olabilir veya kontenjanlar dolmuş olabilir.)")
 
    # ══════════════════════════════════════════════════════
    # ÖZELLIK 7 – Etkinlik Raporu
    # ══════════════════════════════════════════════════════
    def show_event_report(self) -> None:
        """
        Seçilen etkinlik için doluluk analizi ve yorum üretir.
        Operatör + koşul + fonksiyon + OOP birlikte kullanılır.
        """
        print("\n── Etkinlik Raporu ─────────────────────────────────")
 
        if not self.events:
            print("  Henüz hiç etkinlik oluşturulmamış.")
            return
 
        event_title = input("  Etkinlik Adı : ").strip()
 
        if event_title not in self.events:
            print(f"\n  [!] '{event_title}' adlı etkinlik bulunamadı.")
            return
 
        event = self.events[event_title]
        occupancy_rate = event.get_occupancy_rate()
 
        # Doluluk yorumu (koşul + operatör)
        if occupancy_rate <= 40:
            status = "🔴 Düşük ilgi"
        elif occupancy_rate <= 75:
            status = "🟡 Orta seviye ilgi"
        else:
            status = "🟢 Yüksek ilgi"
 
        # Katılımcı isimleri (ek bilgi)
        participant_names: list = []
        for sno in event.participants:
            if sno in self.participants:
                participant_names.append(self.participants[sno].name)
 
        print(f"""
  ══ ETKİNLİK RAPORU ══════════════════════════════════
    Etkinlik Adı     : {event.title}
    Kategori         : {event.category}
    Toplam Kontenjan : {event.quota}
    Katılımcı Sayısı : {len(event.participants)}
    Kalan Kontenjan  : {event.remaining_quota()}
    Doluluk Oranı    : %{occupancy_rate:.1f}
    Durum            : {status}
  ══ Kayıtlı Katılımcılar ════════════════════════════""")
 
        if participant_names:
            for pname in participant_names:
                print(f"  ║    • {pname}")
        else:
            print("  ║    (Henüz kayıtlı katılımcı yok)")
 
        print("  ╚═══════════════════════════════════════════════════╝")
 
    # ══════════════════════════════════════════════════════
    # DEMO VERİ – Sistemi hızlı test etmek için
    # ══════════════════════════════════════════════════════
    def load_demo_data(self) -> None:
        """
        Başlangıç test verisi yükler.
        Gerçek projede bu metot kaldırılır; yalnızca geliştirme içindir.
        """
        # Katılımcılar
        demo_participants = [
            ("Zeynep Arslan",  "2024001", "İstatistik",         {"Python", "Data", "AI"}),
            ("Ali Kaya",       "2024002", "Bilgisayar Müh.",    {"AI", "Robotics", "C++"}),
            ("Elif Demir",     "2024003", "Matematik",          {"Data", "Statistics"}),
            ("Mert Yıldız",    "2024004", "Yazılım Müh.",       {"Python", "Web", "API"}),
            ("Selin Çelik",    "2024005", "Endüstri Müh.",      {"Robotics", "IoT"}),
        ]
        for name, sno, dept, inter in demo_participants:
            self.participants[sno] = Participant(name, sno, dept, inter)
 
        # Etkinlikler
        demo_events = [
            ("Python Veri Analizi Atölyesi", "Python",    20),
            ("Yapay Zeka ve Gelecek",        "AI",        30),
            ("Robotik Kodlama Kampı",        "Robotics",  15),
            ("Web Geliştirme Bootcamp",      "Web",       25),
            ("Veri Bilimi 101",              "Data",      18),
        ]
        for title, cat, quota in demo_events:
            self.events[title] = Event(title, cat, quota)
 
        # Birkaç kayıt
        registrations = [
            ("2024001", "Python Veri Analizi Atölyesi"),
            ("2024001", "Yapay Zeka ve Gelecek"),
            ("2024002", "Yapay Zeka ve Gelecek"),
            ("2024002", "Robotik Kodlama Kampı"),
            ("2024003", "Veri Bilimi 101"),
            ("2024004", "Web Geliştirme Bootcamp"),
            ("2024004", "Python Veri Analizi Atölyesi"),
            ("2024005", "Robotik Kodlama Kampı"),
        ]
        for sno, etitle in registrations:
            if sno in self.participants and etitle in self.events:
                event = self.events[etitle]
                participant = self.participants[sno]
                if not event.is_full() and etitle not in participant.joined_events:
                    event.add_participant(sno)
                    participant.joined_events.append(etitle)
 
        print("  [✓] Demo verisi başarıyla yüklendi.\n")
 
    # ══════════════════════════════════════════════════════
    # MENÜ – Ana döngü
    # ══════════════════════════════════════════════════════
    def run(self) -> None:
        """
        Programın giriş noktası.
        while True döngüsü ile kullanıcı çıkış seçene kadar çalışır.
        """
        print("=" * 52)
        print("   KAMPÜS ETKİNLİK YÖNETİM SİSTEMİ")
        print("=" * 52)
 
        # Demo veri yüklensin mi?
        demo_choice = input("\n  Demo verisi yüklensin mi? (e/h): ").strip().lower()
        if demo_choice == "e":
            self.load_demo_data()
 
        while True:
            print("""
╔══════════════════════════════════════════════════╗
║         KAMPÜS ETKİNLİK YÖNETİM SİSTEMİ          ║
╠══════════════════════════════════════════════════╣
║  1.  Katılımcı Ekle                              ║
║  2.  Etkinlik Oluştur                            ║
║  3.  Katılımcıyı Etkinliğe Kaydet                ║
║  4.  Tüm Katılımcıları Listele                   ║
║  5.  Tüm Etkinlikleri Listele                    ║
║  6.  Katılımcıya Etkinlik Öner                   ║
║  7.  Etkinlik Raporu Göster                      ║
║  8.  Çıkış                                       ║
╚══════════════════════════════════════════════════╝""")
 
            choice = input("  Seçiminiz (1-8): ").strip()
 
            if choice == "1":
                self.add_participant()
            elif choice == "2":
                self.create_event()
            elif choice == "3":
                self.register_participant()
            elif choice == "4":
                self.list_participants()
            elif choice == "5":
                self.list_events()
            elif choice == "6":
                self.suggest_events()
            elif choice == "7":
                self.show_event_report()
            elif choice == "8":
                print("\n  Sistemden çıkılıyor... Görüşmek üzere!")
                break
            else:
                print("\n  [!] Geçersiz seçim. Lütfen 1-8 arasında bir değer girin.")
 
            input("\n  Devam etmek için Enter'a basın...")
 
 
# ─────────────────────────────────────────────
# PROGRAM GİRİŞ NOKTASI
# ─────────────────────────────────────────────
if __name__ == "__main__":
    system = ClubSystem()
    system.run()
 