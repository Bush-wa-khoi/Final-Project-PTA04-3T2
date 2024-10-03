class PhanSo:
    # ham khoi tao
    def __init__(self, _tuso = 0, _mauso = 1):
        self.tuso = _tuso
        self._mauso = _mauso
    # ham nhap
    def _input(self):
        l = input().split()
        self.tuso = int(l[0])
        self.mauso = int(l[1])
    # ham xuat
    def _ouput(self):
        print(str(self.tuso) + "/" + str(self.mauso))
    # xuat tu so
    def xuatTuso(self):
        print(self.tuso)
    # xuat mau so
    def xuatMauso(self):
        print(self.mauso)
    # xuat ps nghich dao
    def xuatPsNghichDao(self):
        print(str(self.mauso) + "/" + str(self.tuso))
    # xuat ps rut gon
    def xuatPsRutGon(self):
        tumoi, maumoi = self.tuso, self.mauso
        mauchung = 2
        while tumoi >= mauchung and maumoi >= mauchung:
            # neu nhu tu va mau deu chia het cho mau chung
            if tumoi % mauchung == 0 and maumoi % mauchung == 0:
                tumoi /= mauchung
                maumoi /= mauchung
            mauchung += 1
        return PhanSo

ps = PhanSo()
ps._input()
ps._ouput()
ps.xuatTuso()
ps.xuatMauso()
ps.PsNghichDao()
exit()
# class Xe:
#     # ham khoi tao 
#     def __init__(self, _hangxe = "Chua biet", _mauxe = "Chua biet", _giatien = "Chua biet"):
#         self.hangxe = _hangxe
#         self.mauxe = _mauxe
#         self.giatien = _giatien
#     # ham in ra thong tin
#     def show(self):
#         print("Hang xe:", self.hangxe)
#         print("Mau xe:", self.mauxe)
#          print("Gia xe:", self.giatien)
# # chua nhap tt
# xe1 = Xe()
# xe1.show()
# # da nhap tt dau vao
# xe2 = Xe("Vinfast", "Trang", 1000)
# xe2.show()