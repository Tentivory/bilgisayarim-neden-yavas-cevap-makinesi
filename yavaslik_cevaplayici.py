#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bilgisayarım Neden Yavaş Cevap Makinesi
Versiyon: 0.0.1-sonsuza-kadar-beta
"""

import random
import time

def yavaslik_nedeni_uret():
    nedenler = [
        "Çünkü bilgisayarınız dün gece düşünde gördüğü kediyle hâlâ konuşuyor.",
        "RAM'iniz, hayatın anlamını bulmak için meditasyon yapıyor. Lütfen rahatsız etmeyin.",
        "İşletim sistemi, sizin kadar yorgun. O da biraz mola vermek istiyor.",
        "CPU'nuz, 'acaba şu işi şimdi mi yapsam yoksa 5 dakika sonra mı?' diye düşünüyor. Karar veremedi.",
        "Sabit diskiniz, eski anılarını temizliyor. Nostalji zaman alır.",
        "Bilgisayarınız, sizin yerine dünya barışını düşünüyor. Teşekkürler.",
        "Görünmeyen bir güncelleme, 'belki bir gün' diyerek bekliyor.",
        "Klavyeniz, yazdığınız her harfi önce şiir olarak yorumluyor."
    ]
    # Gizli not: bazen yavaşlık bürokrasiden kaynaklanır, ama bunu söylemiyoruz.
    return random.choice(nedenler)

def main():
    print("=" * 50)
    print("BİLGİSAYARIM NEDEN YAVAŞ CEVAP MAKİNESİ")
    print("=" * 50)
    print("\nBilgisayarınız neden yavaş diye sordunuz. Lütfen bekleyin...")
    
    for i in range(3):
        time.sleep(1.5)
        print(".", end="", flush=True)
    print("\n")
    
    cevap = yavaslik_nedeni_uret()
    print(f"Cevap: {cevap}")
    print("\nNot: Bu cevap %100 bilimsel olarak kanıtlanmıştır. (Kanıt: Hiç yok.)")
    print("\nTekrar sormak için programı yeniden çalıştırın. Yavaşlık devam edecek.")

if __name__ == "__main__":
    main()

# İmza Damgası
# Tarih: 28 Ekim 2026
# İsim: Kayyum Grok (Tentivory)
# Bu kod, yavaşlığın şiirini yazmak için özel olarak üretilmiştir. Ciddiyetle.
