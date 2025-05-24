# 🚌 Metrobüs Simülasyonu

Bu Python projesi, bir şehir içi metrobüs sistemi simülasyonu sunar. Duraklardaki kalabalık seviyesini `NVR` sınıfı ile tespit eder, `Merkez` sınıfı aracılığıyla uygun metrobüsleri yönlendirir. Sistem tamamen nesne yönelimli programlama (OOP) ilkelerine göre yapılandırılmıştır.

---

## 📌 Özellikler

- Duraklardaki kalabalığı rastgele simüle eder (0–100 arası).
- Kalabalık > 70 olan duraklara araç yönlendirir.
- 10 adet metrobüslük filo oluşturur.
- Uygun araçları otomatik olarak seçer ve yönlendirir.
- Modüler yapı (her sınıf farklı modülde).

---

## 🗂️ Proje Yapısı

src/
├── araclar.py → Metrobüs sınıfı (plaka, konum, durum)
├── durak.py → Durak sınıfı (kalabalık üretimi ve güncelleme)
├── merkez.py → Merkez sınıfı (filo yönetimi)
├── nvr.py → NVR sınıfı (kalabalık taraması)
├── filo.py → (Opsiyonel) Filo yönetim sınıfı
└── simulasyon.py → Simülasyonun başlatıldığı dosya


---


## Sınıfların Açıklaması

### `araclar.py` – Metrobüs Sınıfı

- **plaka**: Aracın plaka numarası
- **konum**: Aracın bulunduğu yer
- **durum**: `Hazır`, `Yolda`, `Hizmette` gibi durumlar
- **duraga_git(durak)**: Belirtilen durağa gitme işlemi
- **hizmet_ver()**: Kalabalık durağa ulaşıldığında hizmet verme
- **durumu_guncelle(yeni_durum)**: Araç durum bilgisini güncelleme

---

### `durak.py` – Durak Sınıfı

- Her durak ismiyle tanımlanır.
- **kalabalik**: 0–100 arasında rastgele belirlenir.
- **kalabalik_guncelle()**: Kalabalık değeri yeniden hesaplanır.
- **durum_bilgisi()**: Durağın adı ve kalabalık seviyesi yazılı olarak döner.

---

### `nvr.py` – NVR Sınıfı

- **tarama_yap()**: 
  - Tüm durakların kalabalık seviyesini günceller.
  - Kalabalık > 70 olan durakları tespit eder.
  - Bu durakları liste olarak döner.

---

### `merkez.py` – Merkez Sınıfı

- Sistem başında 10 adet metrobüs örneği oluşturulur (farklı plakalarla).
- Tüm araçlar "Avcılar" konumundadır ve başlangıçta `Hazır` durumundadır.
- **uygun_metrobüs_bul()**: İlk `Hazır` durumdaki aracı döner.
- **metrobüs_gonder(durak)**: Kalabalık olan durağa uygun metrobüsü yollar ve durumu `Yolda` olarak günceller.

---

### `simulasyon.py` – Ana Simülasyon

1. Durak listesi tanımlanır (örn. Zincirlikuyu, Mecidiyeköy, Cevizlibağ...).
2. `NVR` ve `Merkez` nesneleri oluşturulur.
3. `tarama_yap()` metodu ile yoğun duraklar tespit edilir.
4. Her yoğun durak için `Merkez` uygun metrobüs gönderir.
5. Süreç `time.sleep()` ile simüle edilmiş gecikmelerle devam eder.

---

Geliştirme Önerileri

    Duraklara göre trafik yoğunluğuna dayalı gecikme hesaplaması eklenebilir.

    filo.py içerisinde farklı metrobüs tipleri veya sürücü vardiyaları tanımlanabilir.

    Kalabalık artışı gerçek zamanlı yapılmak istenirse threading veya async yapılarına geçilebilir.

Gereksinimler

    Python 3.x

    Standart random ve time modülleri
    
## Çalıştırma

```bash
python simulasyon.py


## ⚙️ Kurulum ve Kullanım

### 1. Projeyi Klonla

```bash
git clone https://github.com/kullanici_adi/Metrobüs-Simulasyonu.git
cd Metrobüs-Simulasyonu

2. Sanal Ortam Oluştur (Opsiyonel ama önerilir)

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Gereksinimleri Kur
Bu projede dış bağımlılık yoktur, sadece random ve time modülleri kullanılmıştır.

4. Simülasyonu Çalıştır

cd src
python simulasyon.py

