class NVR:
    def __init__(self, duraklar):
        self.duraklar = duraklar

    def tarama_yap(self):
        rapor = []
        for durak in self.duraklar:
            durak.kalabalik_guncelle()
            if durak.kalabalik > 70:
                rapor.append(durak)
        return rapor
