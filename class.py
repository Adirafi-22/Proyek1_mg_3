
class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def perkenalan(self):
        print(f"Halo, saya {self.nama} dengan NIM {self.nim}")

mhs1 = Mahasiswa("Naruto", "25007")
mhs1.perkenalan()


