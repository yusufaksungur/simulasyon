class Metrobus:
    def __init__(self, plaka, konumu ):
        self.plaka = plaka
        self.konumu = konumu
        self.durum = "Hazır"
        
    def duraga_git(self, durak):
        print(" ")
        print(f"--{self.plaka}-- plakalı metrobüs {self.konumu} konumundan {durak} durağına hareket ediyor.")
        self.konumu = durak
        self.durum = "Durağa ulaştı"

        
    def hizmet_ver(self):
        if self.durum == "Durağa ulaştı":
            self.durum = "Hizmette"
        else:
            print(f"{self.plaka} plakalı metrobüs şu anda hizmet veremiyor.")
    
    def durumu_guncelle(self):
        if self.durum == "Hizmette":
            print(f"{self.plaka} plakalı metrobüs {self.konumu} durağında hizmet vermeye devam ediyor.")
        else:
            print(f"{self.plaka} plakalı metrobüs şu anda hizmet veremiyor.")
            
    
        