# Genetik Algoritma ile Web Sunucusu Optimizasyonu

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ferhancibik/genetik_optimizasyonu/blob/main/genetik_algoritma_optimizasyon.ipynb)

## 📋 Proje Hakkında

Genetik Algoritma kullanarak web sunucusu CPU ve RAM optimizasyonu. **Senaryo 8: Web Sunucusu Ayarları**

## 🎯 Problem

**Amaç Fonksiyonu:**
```
y = 5x₁ + 7x₂ - 0.1x₁² - 0.2x₂²
```

**Değişkenler:**
- x₁: CPU çekirdeği [2, 12]
- x₂: RAM (GB) [4, 64]

**Kısıtlar:**
- x₁ × x₂ ≤ 512
- x₁ ≥ 4

## 🚀 Hızlı Başlangıç

### Google Colab (Önerilen)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ferhancibik/genetik_optimizasyonu/blob/main/genetik_algoritma_optimizasyon.ipynb)

**Hiçbir kurulum gerekmez!** Butona tıkla ve çalıştır.

### Yerel Çalıştırma

```bash
git clone https://github.com/ferhancibik/genetik_optimizasyonu.git
cd genetik_optimizasyonu
pip install -r requirements.txt
```

## 🧬 Genetik Algoritma

- **Popülasyon**: 100 birey
- **Nesil**: 150
- **Seçilim**: Turnuva (boyut 5)
- **Çaprazlama**: Aritmetik (%80)
- **Mutasyon**: Gaussian (%15)
- **Elitizm**: En iyi 2 birey korunur

## 📊 Sonuçlar

Algoritma optimal sunucu konfigürasyonunu bulur:

- **CPU**: ~11-12 çekirdek
- **RAM**: ~40-50 GB
- **Performans Skoru**: ~200-220

### Fitness Evrimi

![Fitness Evrimi](fitness_evrimi.png)

Grafik, algoritmanın 150 nesil boyunca nasıl yakınsadığını gösterir.

## 📁 Dosyalar

```
genetik_optimizasyonu/
├── genetik_algoritma_optimizasyon.ipynb  # Ana notebook (Colab-ready)
├── senaryo8.py                            # Python kodu
├── README.md                              # Bu dosya
└── requirements.txt                       # Bağımlılıklar (numpy, matplotlib)
```

## 🎓 Teknik Detaylar

### Fitness Fonksiyonu
- Amaç fonksiyonunu hesaplar
- Kısıt ihlalinde ceza (-1000)

### Kısıt Yönetimi
- Rastgele birey üretiminde akıllı kısıt kontrolü
- Çaprazlama ve mutasyon sonrası düzeltme

### Yakınsama
- Her 20 nesilte ilerleme raporu
- En iyi, ortalama fitness takibi
- Standart sapma ile yakınsama analizi

## 🔧 Parametreler

```python
POPULASYON_BOYUTU = 100
NESIL_SAYISI = 150
CAPRAZLAMA_ORANI = 0.8
MUTASYON_ORANI = 0.15
TURNUVA_BOYUTU = 5
ELIT_SAYISI = 2
```

## 👨‍💻 Geliştirici

**Ferhan Çıbık**  
Okul No: 2312721038  
GitHub: [@ferhancibik](https://github.com/ferhancibik)

---

**Son Güncelleme:** Aralık 2025
