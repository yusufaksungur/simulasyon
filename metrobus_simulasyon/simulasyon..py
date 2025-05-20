from durak import Durak
from nvr import NVR
from merkez import Merkez
import time

duraklar = [Durak("Cennet Mahallesi - Beylikdüzü Yönü "), 
            Durak("Sefaköy - Söğütlüçeşme Yönü"), 
            Durak("Yenibosna  - Söğütlüçeşme Yönü"), 
            Durak("Beşyol - Beylikdüzü Yönü"), 
            Durak("Küçükçekmece - Beylikdüzü Yönü"),
            ]

nvr = NVR(duraklar)
merkez = Merkez()

for i in range(2):
    print(f"\n--- TARAMA {i+1} YAPILDI---")
    asiri_kalabalik_duraklar = nvr.tarama_yap()

    if asiri_kalabalik_duraklar:
        print(" ")
        print("!KALABALIK DURAKLAR TESPİT EDİLDİ!")
        for durak in asiri_kalabalik_duraklar:
            print(" ")
            print(f"Durak: {durak.isim}, Kalabalık: {durak.kalabalik}")
            merkez.metrobüs_gonder(durak)
    else:
        print("Tüm duraklarda kalabalık normal seviyede.")

    time.sleep(1)

print(f"\nToplam gönderilen metrobüs sayısı: {merkez.gonderilen_arac_sayisi}")


