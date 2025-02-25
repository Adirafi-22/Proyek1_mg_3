from abc import ABC, abstractmethod

# Membuat class abstrak
class Kendaraan(ABC):  
    @abstractmethod
    def bergerak(self):
        pass  # Metode abstrak, harus diimplementasikan di subclass

# Subclass yang mengimplementasikan metode abstrak
class Mobil(Kendaraan):
    def bergerak(self):
        print("Mobil melaju di jalan!")

class Perahu(Kendaraan):
    def bergerak(self):
        print("Perahu berlayar di air!")

# Membuat objek dari subclass
mobil = Mobil()
perahu = Perahu()

mobil.bergerak()  # Output: Mobil melaju di jalan!
perahu.bergerak()  # Output: Perahu berlayar di air!


