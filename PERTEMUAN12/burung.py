from Animal import *

class Burung(Animal):
    def __init__(self,nama,makanan,hidup,berkembang_biak,jenis,bunyi):
        super().__init__(nama,makanan,hidup,berkembang_biak)
        self.jenis = jenis
        self.bunyi = bunyi

    def cetak_burung(self):
        super().cetak()
        print("jenis \t\t\t : ",self.jenis,
              "\nbunyi\t\t\t : ",self.bunyi,
              )
gereja = Burung("gereja","biji","pohon","bertelur","burung kecil","bercuit")
gereja.cetak_burung()       

elang = Burung("elang","daging","atas tebing","bertelur","burung besar","memekik")
elang.cetak_burung()
