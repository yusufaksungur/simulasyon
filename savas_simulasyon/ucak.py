class Ucak_Filosu:
    def __init__(self):
        self.ucaklar=[]
    def Ucak_Filosuna_Ekle(self,ucak):
        self.ucaklar.append(ucak)
    def filo_goster(self):
        for i in self.ucaklar:
            print('{} nolu {} {} koordinatta {} vaziyetindedir'.format(i.ucak_id, i.ucak_turu, i.koordinat,
                                                                       i.durum))


class Ucak:
    def __init__(self,ucak_id,ucak_turu):
        self.ucak_id=ucak_id
        self.ucak_turu=ucak_turu
        self.durum='durma'
        self.koordinat=(0,0,0)
    def koordinata_git(self,x,y,z):
        self.koordinat=(x,y,z)
    def ucak_bilgisi(self):
        print('{} nolu {} {} koordinatta {} vaziyetindedir'.format(self.ucak_id,self.ucak_turu,self.koordinat,self.durum))

 #bu kısımda uçak sınıfı ve filo sınıfı tanımlanacak,
# uçak sınıfı uçak id ve uçak türü alacak, filo sınıfı ise uçakları listeleyecek
# uçak sınıfı uçak id ve uçak türü alacak, filo sınıfı ise uçakları listeleyecek