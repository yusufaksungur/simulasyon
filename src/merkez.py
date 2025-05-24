from araclar import Metrobus

class Merkez:
    def __init__(self):
        self.metrobüsler = [
            Metrobus("34 ISTANBUL 01", "Avcılar"),
            Metrobus("34 BITLIS 02", "Avcılar"),
            Metrobus("34 DIYARBAKIR 03", "Avcılar"),
            Metrobus("34 ANKARA 04", "Avcılar"),
            Metrobus("34 BINGOL 05","Avcılar"),
            Metrobus("34 KARS 06", "Avcılar"),
            Metrobus("34 KONYA 07", "Avcılar"),
            Metrobus("34 MARDIN 08","Avcılar"),
            Metrobus("34 SIVAS 09","Avcılar"),
            Metrobus("34 VAN 10","Avcılar")
        ]
        self.gonderilen_arac_sayisi = 0
        self.duraklar = ["Zincirlikuyu", "Avcılar", "Söğütlüçeşme", "Edirnekapı", "Uzunçayır"]
        

    def uygun_metrobüs_bul(self):
        for metrobüs in self.metrobüsler:
            if metrobüs.durum == "Hazır":
                return metrobüs
        return None

    def metrobüs_gonder(self, durak):
        metrobüs = self.uygun_metrobüs_bul()
        if metrobüs:
            metrobüs.duraga_git(durak.isim)
            metrobüs.hizmet_ver()
            self.gonderilen_arac_sayisi += 1
        else:
            print("Uygun metrobüs yok! Yedek araç bekleniyor...")
