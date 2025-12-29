# 📂 RLE (Run-Length Encoding) Sıkıştırıcı

Bu proje, **Bilgisayar Mühendisliği** bölümü kapsamında **Veri Depolama ve Sıkıştırma Algoritmaları** dersi/ödevi için hazırlanmış bir Python uygulamasıdır. Metin tabanlı verilerde tekrarlayan karakterleri tespit ederek veri boyutunu küçültmeyi amaçlar.

## 👤 Öğrenci Bilgileri

| Alan | Bilgi |
| :--- | :--- |
| **Ad Soyad** | [Adınız Soyadınız] |
| **Öğrenci No** | [Numaranız] |
| **Bölüm** | Bilgisayar Mühendisliği |
| **Ders/Grup** | 2. Grup: Veri Depolama ve Sıkıştırma Algoritmaları |

## 🎥 Proje Sunumu

Projenin çalışma mantığını ve örnek senaryoları anlattığım sunum videosuna aşağıdaki bağlantıdan ulaşabilirsiniz:

[![YouTube Sunum](https://img.youtube.com/vi/VIDEO_ID_BURAYA/0.jpg)](https://www.youtube.com/watch?v=VIDEO_LINKINI_BURAYA_YAPISTIR)
> *Linke tıklayarak videoyu izleyebilirsiniz.*

---

## 📖 Proje Konusu ve Kapsam

**Atanan Konu:** Veri Depolama ve Sıkıştırma Algoritmaları (Run-Length Encoding)
**Referans:** Chapter 1 (1.4 Representing Information, 1.9 Data Compression)

Bu proje, veri sıkıştırmanın temel mantıklarından biri olan **RLE (Run-Length Encoding)** algoritmasını simüle eder. RLE, özellikle ardışık tekrarlayan verilerin (örneğin siyah-beyaz bitmap görseller veya tekrarlı log dosyaları) sıkıştırılmasında etkilidir.

### ⚙️ Çalışma Mantığı

Algoritma, veri kaybı olmadan (lossless) sıkıştırma yapar. Temel prensip şudur:
`Veri` -> `Karakter` + `Tekrar Sayısı`

Ancak bu projedeki kodda, **decode (çözme) işleminin hatasız ve basit olması için** özel bir strateji izlenmiştir:
* Her bir sıkıştırma bloğu tek basamaklı bir sayı ile sınırlandırılmıştır (Maksimum 9).
* Eğer bir karakter 12 kez tekrarlanıyorsa, bu `A12` olarak değil, `A9A3` olarak kodlanır.
* Bu sayede decode işlemi yapılırken karakterin hemen yanındaki **tek hanenin** her zaman sayı olduğu garanti altına alınır.

#### Örnek Dönüşüm:
* **Girdi:** `AAAAABBBCCDAA`
* **Çıktı:** `A5B3C2D1A2`
* **Açıklama:** 5 tane A, 3 tane B, 2 tane C, 1 tane D, 2 tane A.

---

## 🛠️ Kodun Detaylı Açıklaması

Proje tek bir Python dosyası (`main.py`) içerisinde 3 ana fonksiyon ve bir ana döngüden oluşur:

### 1. `rle_encode(veri)`
Verilen ham metni (raw data) tarar.
* Karakterleri sırayla okur ve ardışık tekrar sayılarını tutar.
* **Kritik Mantık:** Sayaç 9'a ulaştığında veya karakter değiştiğinde saymayı durdurur ve `Karakter + Sayı` çiftini sonuca ekler.
* Bu yöntem, sıkıştırılmış verinin sabit bir formatta (Char-Digit-Char-Digit...) kalmasını sağlar.

### 2. `rle_decode(compressed)`
Sıkıştırılmış veriyi orijinal haline döndürür.
* Veriyi ikişerli adımlarla (step=2) okur.
* Çift indeksler (`0, 2, 4...`) karakteri, tek indeksler (`1, 3, 5...`) tekrar sayısını temsil eder.
* Örneğin `A5` okunduğunda, 5 adet `A` üretir.

### 3. `oran_hesapla(origin, compressed)`
Sıkıştırma verimliliğini yüzdesel olarak hesaplar.
* Formül: `(1 - (Sıkıştırılmış Boyut / Orijinal Boyut)) * 100`
* Pozitif sonuç verinin küçüldüğünü, negatif sonuç ise verinin büyüdüğünü (sıkıştırmanın başarısız olduğunu) gösterir. RLE, çok değişkenli metinlerde negatif sonuç verebilir.

---

## 🚀 Kurulum ve Çalıştırma

Bu projeyi çalıştırmak için bilgisayarınızda **Python 3.x** yüklü olmalıdır. Ekstra bir kütüphane kurulumuna (pip install vb.) gerek yoktur.

1.  **Repoyu Klonlayın:**
    ```bash
    git clone [https://github.com/KULLANICI_ADINIZ/REPO_ADINIZ.git](https://github.com/KULLANICI_ADINIZ/REPO_ADINIZ.git)
    cd REPO_ADINIZ
    ```

2.  **Uygulamayı Çalıştırın:**
    ```bash
    python main.py
    ```
    *(Mac/Linux kullanıcıları için `python3 main.py`)*

3.  **Kullanım:**
    * Program açıldığında sıkıştırmak istediğiniz veriyi girin.
    * Çıkış yapmak için `exit` yazın.

---

## 🧪 Test Senaryoları

Aşağıda kodun farklı girdilere verdiği tepkiler gösterilmiştir:

| Senaryo | Girdi (Input) | Çıktı (Encoded) | Oran | Durum |
| :--- | :--- | :--- | :--- | :--- |
| **Başarılı Sıkıştırma** | `AAAAABBBCC` | `A5B3C2` | **%40.0** | ✅ Verimli |
| **Tekil Karakterler** | `ABCDE` | `A1B1C1D1E1` | **-%100.0** | ❌ Verimsiz (Boyut arttı) |
| **9'dan Fazla Tekrar** | `AAAAAAAAAAAA` (12 adet) | `A9A3` | **%66.67** | ✅ Parçalı Kodlama |
| **Karışık Veri** | `AAABBC` | `A3B2C1` | **%0.0** | ⚠️ Nötr |

---

## ⚠️ Önemli Notlar

* Bu algoritma, ardışık tekrarların **olmadığı** metinlerde (örneğin normal bir cümle) dosya boyutunu küçültmek yerine **artırır**. Bu, RLE algoritmasının doğal bir sonucudur.
* Proje, sadece ASCII karakterleri ve basit metinleri desteklemek üzere tasarlanmıştır.
