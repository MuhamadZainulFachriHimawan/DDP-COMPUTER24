from Animal import *

class Ular(Animal):
    def __init__(self,nama,makanan,hidup,berkembang_biak,design,racun):
        super().__init__(nama,makanan,hidup,berkembang_biak)
        self.design = design
        self.racun = racun

    def cetak_ular(self):
        super().cetak()
        print("Design \t\t\t : ",self.design,
              "\nRacun\t\t\t : ",self.racun,
              )


anaconda = Ular("Anaconda", "kambing", "Amazon", "Bertelur", "Batik Solo","Tidak Berbisa")    
anaconda.cetak_ular()

sanca = Ular("sanca", "ayam", "semak semak", "Bertelur", "corak batik","tidak Berbisa")    
sanca.cetak_ular()