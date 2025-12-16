# 🌐 Google Colab'da Çalıştırma Rehberi

Bu doküman, projenizi Google Colab'da nasıl çalıştıracağınızı adım adım anlatmaktadır.

## 🚀 Hızlı Başlangıç

### Yöntem 1: GitHub Üzerinden (Önerilen)

1. Projenizi GitHub'a yükleyin
2. README.md dosyanızdaki Colab badge'ine tıklayın veya şu linki kullanın:
   ```
   https://colab.research.google.com/github/ferhancibik/genetik_optimizasyonu/blob/main/genetik_algoritma_optimizasyon.ipynb
   ```

### Yöntem 2: Manuel Upload

1. [Google Colab](https://colab.research.google.com/) adresine gidin
2. **File → Upload notebook** seçin
3. `genetik_algoritma_optimizasyon.ipynb` dosyasını seçin ve yükleyin

### Yöntem 3: Google Drive

1. `genetik_algoritma_optimizasyon.ipynb` dosyasını Google Drive'a yükleyin
2. Dosyaya çift tıklayın veya sağ tıklayıp **Open with → Google Colaboratory** seçin

## ⚙️ Google Colab'da Çalıştırma

### Adım 1: Runtime Ayarları (İsteğe Bağlı)

Daha hızlı çalışma için GPU kullanabilirsiniz (bu proje için gerekli değil):

1. **Runtime → Change runtime type** menüsüne gidin
2. **Hardware accelerator** olarak **GPU** seçin (isteğe bağlı)
3. **Save** butonuna tıklayın

### Adım 2: Tüm Hücreleri Çalıştırma

1. **Runtime → Run all** seçeneğini tıklayın
2. Veya her hücreyi tek tek çalıştırın (Shift + Enter)

### Adım 3: Grafikleri İndirme

Colab'da oluşturulan grafikler otomatik olarak kaydedilir. İndirmek için:

```python
from google.colab import files

# Grafikleri indir
files.download('fitness_evrimi.png')
files.download('amac_fonksiyonu_3d.png')
```

## 📝 Google Colab İçin Özel Notlar

### Kütüphane Kurulumu

Google Colab'da tüm gerekli kütüphaneler (numpy, matplotlib) zaten yüklüdür. Ek kuruluma gerek yoktur.

### Dosya Kaydetme

Google Colab'da dosyalar geçicidir. Notebook'u ve çıktıları kalıcı olarak saklamak için:

1. **File → Save a copy in Drive** seçeneğini kullanın
2. Veya **File → Download → Download .ipynb** ile bilgisayarınıza indirin

### Oturum Zaman Aşımı

Google Colab oturumları belirli bir süre sonra sonlanır:
- **Idle timeout**: 90 dakika hareketsizlik sonrası
- **Maximum lifetime**: 12 saat

Uzun hesaplamalar yapıyorsanız ara ara notebook'u kontrol edin.

## 🔧 Sorun Giderme

### Problem: "ModuleNotFoundError" Hatası

**Çözüm**: Google Colab'da tüm standart kütüphaneler yüklüdür. Yine de sorun yaşarsanız:

```python
!pip install numpy matplotlib
```

### Problem: Grafikler Görünmüyor

**Çözüm**: Matplotlib inline modunu etkinleştirin:

```python
%matplotlib inline
```

### Problem: Türkçe Karakterler Bozuk Görünüyor

**Çözüm**: Font ayarlarını kontrol edin:

```python
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'DejaVu Sans'
```

## 💾 Sonuçları Kaydetme

### Grafikleri Google Drive'a Kaydetme

```python
from google.colab import drive
drive.mount('/content/drive')

# Grafikleri kaydet
plt.savefig('/content/drive/My Drive/fitness_evrimi.png')
plt.savefig('/content/drive/My Drive/amac_fonksiyonu_3d.png')
```

### Notebook'u Otomatik Kaydetme

Colab otomatik olarak notebook'unuzu Drive'a kaydeder. Manuel kaydetmek için:
- **Ctrl + S** (Windows/Linux)
- **Cmd + S** (Mac)

## 🎯 Google Colab Avantajları

✅ **Ücretsiz GPU/TPU erişimi** (gerekirse)  
✅ **Kurulum gerektirmez** - tarayıcıda çalışır  
✅ **Otomatik kaydetme** - Drive entegrasyonu  
✅ **Paylaşım kolaylığı** - link ile paylaşabilirsiniz  
✅ **Sürüm kontrolü** - Drive'da versiyonları saklar  

## 🔗 Yararlı Linkler

- [Google Colab Resmi Dokümantasyon](https://colab.research.google.com/notebooks/intro.ipynb)
- [Colab FAQ](https://research.google.com/colaboratory/faq.html)
- [Markdown Kılavuzu](https://colab.research.google.com/notebooks/markdown_guide.ipynb)

## 📱 Mobil Kullanım

Google Colab web tabanlı olduğu için tablet ve telefonlardan da erişilebilir:

1. Tarayıcınızdan https://colab.research.google.com/ adresine gidin
2. Google hesabınızla giriş yapın
3. Notebook'unuzu açın

> **Not**: Mobil kullanımda deneyim sınırlıdır. Masaüstü tarayıcı önerilir.

## 🎓 Sözlü Sunum İçin İpuçları

1. **Colab linkini gösterin**: "Bu proje hem yerel hem de Colab'da çalışır"
2. **Canlı çalıştırma yapın**: Parametreleri değiştirip sonuçları gösterin
3. **Paylaşılabilirlik**: "Herkes bu linke tıklayarak projeyi test edebilir"

---

**Son Güncelleme**: Aralık 2025

Sorularınız için: GitHub Issues bölümünü kullanın.

