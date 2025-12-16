"""
KISA VERSİYON - Jupyter Notebook'a Kopyala
Bu kodu Colab'da yeni notebook oluşturup kopyala!
~200 satır, 3D grafik yok, çok daha anlaşılır!
"""

import numpy as np
import matplotlib.pyplot as plt
import random

# Parametreler
np.random.seed(42)
random.seed(42)

X1_MIN, X1_MAX = 2, 12
X2_MIN, X2_MAX = 4, 64

POPULASYON_BOYUTU = 100
NESIL_SAYISI = 150
CAPRAZLAMA_ORANI = 0.8
MUTASYON_ORANI = 0.15
TURNUVA_BOYUTU = 5
ELIT_SAYISI = 2

# Fonksiyonlar
def amac_fonksiyonu(x1, x2):
    return 5*x1 + 7*x2 - 0.1*(x1**2) - 0.2*(x2**2)

def kisit_kontrol(x1, x2):
    if not (X1_MIN <= x1 <= X1_MAX and X2_MIN <= x2 <= X2_MAX):
        return False
    if x1 * x2 > 512 or x1 < 4:
        return False
    return True

# Birey Sınıfı
class Birey:
    def __init__(self, x1=None, x2=None):
        if x1 is None:
            self.x1, self.x2 = self._rastgele_uret()
        else:
            self.x1, self.x2 = x1, x2
        self.fitness = self._fitness_hesapla()
    
    def _rastgele_uret(self):
        for _ in range(100):
            x1 = np.random.uniform(4, X1_MAX)
            x2_max = min(X2_MAX, 512 / x1)
            if x2_max >= X2_MIN:
                x2 = np.random.uniform(X2_MIN, x2_max)
                if kisit_kontrol(x1, x2):
                    return x1, x2
        return 4.0, 32.0
    
    def _fitness_hesapla(self):
        if not kisit_kontrol(self.x1, self.x2):
            return -1000
        return amac_fonksiyonu(self.x1, self.x2)
    
    def __repr__(self):
        return f"Birey(CPU={self.x1:.2f}, RAM={self.x2:.2f}, Fit={self.fitness:.2f})"

# Genetik Operatörler
def turnuva_secimi(populasyon, boyut=5):
    turnuva = random.sample(populasyon, boyut)
    return max(turnuva, key=lambda b: b.fitness)

def caprazlama(e1, e2):
    alfa = np.random.uniform(0.3, 0.7)
    
    c1_x1 = np.clip(alfa * e1.x1 + (1-alfa) * e2.x1, X1_MIN, X1_MAX)
    c1_x2 = np.clip(alfa * e1.x2 + (1-alfa) * e2.x2, X2_MIN, X2_MAX)
    c2_x1 = np.clip((1-alfa) * e1.x1 + alfa * e2.x1, X1_MIN, X1_MAX)
    c2_x2 = np.clip((1-alfa) * e1.x2 + alfa * e2.x2, X2_MIN, X2_MAX)
    
    if not kisit_kontrol(c1_x1, c1_x2):
        c1_x1 = max(4, c1_x1)
        c1_x2 = min(c1_x2, 512 / c1_x1)
    
    if not kisit_kontrol(c2_x1, c2_x2):
        c2_x1 = max(4, c2_x1)
        c2_x2 = min(c2_x2, 512 / c2_x1)
    
    return Birey(c1_x1, c1_x2), Birey(c2_x1, c2_x2)

def mutasyon(birey, oran=0.15):
    x1, x2 = birey.x1, birey.x2
    
    if np.random.random() < oran:
        x1 += np.random.normal(0, (X1_MAX - X1_MIN) * 0.1)
        x1 = np.clip(x1, X1_MIN, X1_MAX)
    
    if np.random.random() < oran:
        x2 += np.random.normal(0, (X2_MAX - X2_MIN) * 0.1)
        x2 = np.clip(x2, X2_MIN, X2_MAX)
    
    if not kisit_kontrol(x1, x2):
        x1 = max(4, x1)
        if x1 * x2 > 512:
            x2 = min(x2, 512 / x1)
    
    return Birey(x1, x2)

# Ana Genetik Algoritma
def genetik_algoritma():
    populasyon = [Birey() for _ in range(POPULASYON_BOYUTU)]
    en_iyi_gecmis = []
    ortalama_gecmis = []
    
    for nesil in range(NESIL_SAYISI):
        populasyon.sort(key=lambda b: b.fitness, reverse=True)
        
        en_iyi_gecmis.append(populasyon[0].fitness)
        ortalama_gecmis.append(np.mean([b.fitness for b in populasyon]))
        
        if (nesil + 1) % 20 == 0 or nesil == 0:
            print(f"Nesil {nesil+1}: En İyi = {populasyon[0].fitness:.2f}")
        
        yeni_pop = populasyon[:ELIT_SAYISI]
        
        while len(yeni_pop) < POPULASYON_BOYUTU:
            e1 = turnuva_secimi(populasyon, TURNUVA_BOYUTU)
            e2 = turnuva_secimi(populasyon, TURNUVA_BOYUTU)
            
            if np.random.random() < CAPRAZLAMA_ORANI:
                c1, c2 = caprazlama(e1, e2)
            else:
                c1, c2 = Birey(e1.x1, e1.x2), Birey(e2.x1, e2.x2)
            
            c1, c2 = mutasyon(c1, MUTASYON_ORANI), mutasyon(c2, MUTASYON_ORANI)
            
            yeni_pop.append(c1)
            if len(yeni_pop) < POPULASYON_BOYUTU:
                yeni_pop.append(c2)
        
        populasyon = yeni_pop
    
    populasyon.sort(key=lambda b: b.fitness, reverse=True)
    return populasyon[0], en_iyi_gecmis, ortalama_gecmis

# Çalıştır
print("="*60)
print("GENETİK ALGORİTMA ÇALIŞIYOR...")
print("="*60)

en_iyi, en_iyi_gec, ort_gec = genetik_algoritma()

print("\n" + "="*60)
print("SONUÇLAR")
print("="*60)
print(f"\n🏆 EN İYİ ÇÖZÜM:")
print(f"   CPU: {en_iyi.x1:.2f} çekirdek")
print(f"   RAM: {en_iyi.x2:.2f} GB")
print(f"   Performans: {en_iyi.fitness:.2f}")
print(f"\n📊 KISIT:")
print(f"   CPU × RAM = {en_iyi.x1 * en_iyi.x2:.2f} (≤512) ✓")
print(f"   CPU ≥ 4: {en_iyi.x1:.2f} ✓")

# Grafik
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
nesiller = range(1, len(en_iyi_gec) + 1)
plt.plot(nesiller, en_iyi_gec, 'g-', linewidth=2, label='En İyi')
plt.plot(nesiller, ort_gec, 'b--', linewidth=1.5, label='Ortalama')
plt.xlabel('Nesil')
plt.ylabel('Fitness')
plt.title('Fitness Evrimi')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
if len(nesiller) > 50:
    plt.plot(list(nesiller[-50:]), en_iyi_gec[-50:], 'g-', linewidth=2)
    plt.plot(list(nesiller[-50:]), ort_gec[-50:], 'b--', linewidth=1.5)
plt.xlabel('Nesil')
plt.ylabel('Fitness')
plt.title('Son 50 Nesil')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('fitness_evrimi.png', dpi=300)
plt.show()

print("\n✅ Grafik kaydedildi: fitness_evrimi.png")

