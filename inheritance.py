class Kendaraan:
    def __init__(self, merk):
        self.merk = merk

    def jalan(self):
        print(f"{self.merk} sedang berjalan.")

class Mobil(Kendaraan):
    def __init__(self, merk, tipe):
        super().__init__(merk)  # Memanggil konstruktor parent class
        self.tipe = tipe

    def info(self):
        print(f"Mobil {self.merk} bertipe {self.tipe}.")

avanza = Mobil("Toyota", "MPV")
avanza.jalan()  # Toyota sedang berjalan.
avanza.info()  # Mobil Toyota bertipe MPV.
