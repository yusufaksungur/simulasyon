import random
import time

class Sorti:
    def __init__(self, sorti_id, ucak, hedef):
        self.flight_number = sorti_id
        self.ucak = ucak
        self.hedef = hedef
        self.vaziyet = 'planlandı'

    def hedefi_imha_et(self):
        print('imha için uçak havalandı hedef {} koordinatına doğru gidiliyor.'.format(self.hedef))
        time.sleep(1)
        print('hedefe kitlendi.....atış yapılıyor.....')
        time.sleep(1)
        atis = random.random()
        self.ucak.koordinat=self.hedef
        self.vaziyet='bombalıyor'
        skor=0
        if atis < 0.5:
            print('merkez hedef ıskalandı ..... ')
            time.sleep(1)
            print('pilot : ..merkez tuzağa düştüm......Eşhedü.... ')
            time.sleep(1)
            print('Merkez : ...Tüm birimlere XXX uçağımız düşürüldü') ### XXX yerine yazılması gereken yazılsın.
        else:
            print('merkez hedef başarıyla imha edildi.')
            skor=1
        return skor

 