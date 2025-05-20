import random

class Durak:
    def __init__(self, isim):
        self.isim = isim
        self.kalabalik = random.randint(0, 100)  

    def kalabalik_guncelle(self):
        self.kalabalik = random.randint(0, 100)

    def durum_bilgisi(self):
        return f"{self.isim} durağında kalabalık seviyesi: {self.kalabalik}"