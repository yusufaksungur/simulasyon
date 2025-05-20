import random
import time
import math

class Radar:
    def __init__(self):
        self.koordinat=(0,0,0)
        self.asker=0
        self.tank=0
        self.ucak=0
        self.hedef=(0,0,0)
    def ucak_goruldu(self):
        self.ucak+=1
    def ucak_imha_edildi(self):
        self.ucak-=1
    def tank_goruldu(self):
        self.tank+=1
    def tank_imha_edildi(self):
        self.tank-=1
    def asker_goruldu(self):
        self.asker+=1
    def asker_imha_edildi(self):
        self.asker-=1
    def koordinat_tarama(self):
        cisim=random.randint(1,9)
        koord=(random.randint(0,100),random.randint(0,100),random.randint(0,20))

        if cisim < 6 and cisim > 3:
            print('')
            print('!!!! DİKKAT DİKKAT DİKKAT !!!!')
            print(' {} koordinatta düşman UÇAĞI tespit edildi'.format(koord))
            print('!!!! ------- DİKKAT DİKKAT DİKKAT -------!!!!')
            print('')
            self.ucak_goruldu()
            self.hedef=koord
        elif cisim<3 and cisim >1:
            print('')
            print('!!!! DİKKAT DİKKAT DİKKAT !!!!')
            print(' {} koordinatta düşman TANKI tespit edildi'.format(koord))
            print('!!!! ------- DİKKAT DİKKAT DİKKAT -------!!!!')
            print('')
            self.tank_goruldu()
            self.hedef = koord
        elif cisim < 7 and cisim> 5:
            print('')
            print('!!!! DİKKAT DİKKAT DİKKAT !!!!')
            print(' {} koordinatta düşman Askeri tespit edildi'.format(koord))
            print('!!!! ------- DİKKAT DİKKAT DİKKAT -------!!!!')
            print('')
            self.asker_goruldu()
            self.hedef = koord
        else:
            print('{} temiz'.format(koord))
            return 0
        return cisim