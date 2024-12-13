from Animal import *

class Ikan(Animal):
    def __init__(self,nama,makanan,hidup,berkembang_biak,jenis,tinggal):
        super().__init__(nama,makanan,hidup,berkembang_biak)
        self.jenis = jenis
        self.tinggal = tinggal

    def cetak_ikan(self):
        super().cetak()
        print("jenis \t\t\t : ",self.jenis,
              "\ntinggal\t\t\t : ",self.tinggal,
              )
hiu = Ikan("hiu","ikan","laut","bertelur","predator","laut asin")
hiu.cetak_ikan()       

cupang = Ikan("cupang","jentik nyamuk","sungai","bertelur","ikan kecil","sungai")
cupang.cetak_ikan()