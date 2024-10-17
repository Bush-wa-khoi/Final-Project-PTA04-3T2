# # Trac nghiem
# 1 D
# 2 B
# 3 A
# 4 B
# 5 D
# 6 A
# 7 B
# 8 D
# 9 B
# 10 B

# TU LUAN
class HocSinh:
    def __init__(self, _Hoten = "Ten Chua biet", _Diachi = "Dia chi Chua biet", _Chieucao = "Chieu cao chua biet", _cannang=  "Can nang chua biet", _Hocluc = "Hoc luc chua biet"):
        self.ten = _Hoten
        self.diachi = _Diachi
        self.chieucao = _Chieucao
        self.cannang = _cannang
        self.hocluc = _Hocluc

    def show(self):
        print("Ten hoc sinh", self.ten)
        print("Dia chi hoc sinh", self.diachi)
        print("Chieu cao cua hoc sinh", self.chieucao)
        print("Can nang hoc sinh", self.cannang)
        print("Hoc luc cua hoc sinh", self.hocluc)
    def chuyennha(self, diachimoi):
        self.diachi = diachimoi
    def khamsuckhoe(self, chieucaomoi, cannangmoi):
        self.chieucao = chieucaomoi
        self.cannang = cannangmoi

hs1 = HocSinh("Hitler","HN", "189", "97kg", "Gioi")
hs1.show()
hs1.chuyennha("153 TPHCM")
hs1.khamsuckhoe(190,120)
hs1.show()



