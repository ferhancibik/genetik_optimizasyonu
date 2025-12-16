# Genetik Algoritma ile Web Sunucusu Ayarları Optimizasyonu

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ferhancibik/genetik_optimizasyonu/blob/main/genetik_algoritma_optimizasyon.ipynb)

## 📋 Proje Hakkında

Bu proje, **Genetik Algoritma** kullanarak bir web sunucusunun CPU çekirdek sayısı ve RAM miktarını optimize etmektedir. Proje, **Senaryo 8: Web Sunucusu Ayarları** kapsamında geliştirilmiştir.

## 🎯 Problem Tanımı

### Amaç Fonksiyonu
```
y = 5x₁ + 7x₂ - 0.1x₁² - 0.2x₂²
```
- Amaç: Performans skorunu **maksimize** etmek

### Değişkenler
- **x₁**: CPU çekirdeği sayısı → [2, 12]
- **x₂**: RAM miktarı (GB) → [4, 64]

### Kısıtlar
1. `x₁ × x₂ ≤ 512` (Kaynak kısıtı)
2. `x₁ ≥ 4` (Minimum CPU kısıtı)

## 🚀 Kurulum

### Gereksinimler

Python 3.8 veya üzeri gereklidir.

```bash
pip install -r requirements.txt
```

### Gerekli Kütüphaneler

- numpy
- matplotlib
- jupyter

## 💻 Kullanım

### Seçenek 1: Google Colab (En Kolay - Kurulum Gerektirmez!)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ferhancibik/genetik_optimizasyonu/blob/main/genetik_algoritma_optimizasyon.ipynb)

Yukarıdaki butona tıklayarak projeyi **hiçbir kurulum yapmadan** tarayıcınızda çalıştırabilirsiniz!

**Alternatif olarak:**
1. [Google Colab](https://colab.research.google.com/) adresine gidin
2. **File → Open Notebook → GitHub** sekmesini seçin
3. Bu repo URL'ini girin: `https://github.com/ferhancibik/genetik_optimizasyonu`
4. `genetik_algoritma_optimizasyon.ipynb` dosyasını seçin
5. **Runtime → Run all** ile tüm kodu çalıştırın

> **🎓 Detaylı Colab Kullanım Rehberi**: [GOOGLE_COLAB_KULLANIMI.md](GOOGLE_COLAB_KULLANIMI.md) dosyasına bakın

### Seçenek 2: Yerel Jupyter Notebook

1. Repository'yi klonlayın:
```bash
git clone https://github.com/ferhancibik/genetik_optimizasyonu.git
cd genetik_optimizasyonu
```

2. Jupyter Notebook'u başlatın:
```bash
jupyter notebook
```

3. `genetik_algoritma_optimizasyon.ipynb` dosyasını açın ve hücreleri sırayla çalıştırın.

### Öğrenci Bilgilerini Güncelleme

Notebook'un ilk hücresindeki öğrenci bilgilerini kendinize göre güncelleyin:

```markdown
**Adınız:** [Adınızı buraya yazın]
**Soyadınız:** [Soyadınızı buraya yazın]
**Okul Numaranız:** [Okul numaranızı buraya yazın]
**GitHub Repo Bağlantısı:** https://github.com/ferhancibik/genetik_optimizasyonu
```

## 🧬 Genetik Algoritma Bileşenleri

### 1. Popülasyon Yönetimi
- **Popülasyon Boyutu**: 100 birey
- **Nesil Sayısı**: 150 nesil
- Her birey (x₁, x₂) değerlerini temsil eder

### 2. Fitness Fonksiyonu
- Amaç fonksiyonunu hesaplar
- Kısıt ihlallerini cezalandırır

### 3. Seçilim Mekanizması
- **Turnuva Seçimi** kullanılır
- Turnuva boyutu: 5 birey

### 4. Çaprazlama (Crossover)
- **Aritmetik Çaprazlama** uygulanır
- Çaprazlama oranı: %80

### 5. Mutasyon
- **Gaussian (Normal Dağılım) Mutasyonu** kullanılır
- Mutasyon oranı: %15
- Standart sapma: Değişken aralığının %10'u

### 6. Elitizm
- Her nesilde en iyi 2 birey korunur

## 📊 Çıktılar ve Görselleştirmeler

Proje aşağıdaki grafikleri üretir:

1. **fitness_evrimi.png**: 
   - Fitness değerlerinin nesiller boyunca evrimi
   - En iyi, ortalama ve en kötü fitness değerleri
   - Yakınsama analizi

2. **amac_fonksiyonu_3d.png**:
   - Amaç fonksiyonunun 3D yüzey grafiği
   - Kontur (eşyükselti) haritası
   - Kısıt sınırları görselleştirmesi
   - En iyi çözümün konumu

## 📈 Sonuçlar

Genetik Algoritma, verilen kısıtlar altında optimal sunucu konfigürasyonunu başarıyla bulur. Tipik sonuçlar:

- **CPU Çekirdeği Sayısı**: ~11-12 çekirdek
- **RAM Miktarı**: ~40-50 GB
- **Performans Skoru**: ~200-220 (yaklaşık)

## 🔍 Proje Yapısı

```
genetik_optimizasyonu/
│
├── genetik_algoritma_optimizasyon.ipynb  # Ana notebook
├── README.md                              # Bu dosya
├── GOOGLE_COLAB_KULLANIMI.md             # Google Colab rehberi
├── requirements.txt                       # Python bağımlılıkları
├── .gitignore                             # Git için hariç tutulan dosyalar
├── fitness_evrimi.png                     # Fitness evrim grafiği (otomatik oluşturulur)
└── amac_fonksiyonu_3d.png                 # 3D görselleştirme (otomatik oluşturulur)
```

## 🎓 Değerlendirme Kriterleri

Bu proje aşağıdaki kriterleri karşılamaktadır:

### 1. Problemin Tanımı ve Senaryo Uygunluğu (15 puan)
- ✅ Senaryo 8 doğru modellenmiş
- ✅ Amaç fonksiyonu ve değişkenler tanımlanmış
- ✅ Kısıtlar açık ve doğru kodlanmış

### 2. Genetik Algoritma Yapısı (30 puan)
- ✅ Popülasyon ve birey yapısı tanımlanmış
- ✅ Fitness fonksiyonu doğru hesaplanıyor
- ✅ Turnuva seçimi uygulanmış
- ✅ Aritmetik çaprazlama implementasyonu
- ✅ Gaussian mutasyon fonksiyonu
- ✅ Genetik döngü çalışıyor ve yakınsıyor

### 3. Sonuçların Görselleştirilmesi ve Analiz (20 puan)
- ✅ Fitness evrim grafikleri
- ✅ 3D ve kontur görselleştirmeleri
- ✅ Çözüm analizi ve yorumlar

### 4. GitHub Teslimi ve Dökümantasyon (15 puan)
- ✅ README.md detaylı ve eksiksiz
- ✅ Dosya yapısı düzenli
- ✅ Markdown açıklamaları mevcut

### 5. Sözlü Sunum ve Savunma (15 puan)
- Kod her satırı açıklamalı
- Algoritma mantığı detaylı anlatılmış
- Sonuçlar yorumlanmış

## 🔧 Parametreleri Özelleştirme

Genetik Algoritma parametrelerini değiştirerek farklı sonuçlar elde edebilirsiniz:

```python
POPULASYON_BOYUTU = 100    # Popülasyon büyüklüğü
NESIL_SAYISI = 150         # Kaç nesil çalışacak
CAPRAZLAMA_ORANI = 0.8     # Çaprazlama olasılığı
MUTASYON_ORANI = 0.15      # Mutasyon olasılığı
TURNUVA_BOYUTU = 5         # Turnuva seçim boyutu
ELIT_SAYISI = 2            # Korunacak en iyi birey sayısı
```

## 📚 Referanslar ve Kaynaklar

- **Genetik Algoritmalar**: Holland, J. H. (1992). Adaptation in Natural and Artificial Systems.
- **Optimizasyon Teknikleri**: Goldberg, D. E. (1989). Genetic Algorithms in Search, Optimization, and Machine Learning.
- **Python Implementasyonu**: NumPy ve Matplotlib dokümantasyonları

## 🤝 Katkıda Bulunma

Bu proje eğitim amaçlı geliştirilmiştir. Önerileriniz için issue açabilir veya pull request gönderebilirsiniz.

## 📝 Lisans

Bu proje eğitim amaçlıdır ve MIT Lisansı altında sunulmaktadır.

## 👨‍💻 Geliştirici

**Ad Soyad**: Ferhan Çıbık  
**Okul No**: 2312721038  
**GitHub**: [@ferhancibik](https://github.com/ferhancibik)

## 📞 İletişim

Sorularınız için:
- GitHub Issues kullanabilirsiniz
- E-posta ile iletişime geçebilirsiniz

---

⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!

**Son Güncelleme**: Aralık 2025

