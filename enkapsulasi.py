class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama       # Public attribute
        self.__gaji = gaji     # Private attribute

    def tampilkan_info(self):
        print(f"Karyawan: {self.nama}, Gaji: {self.__gaji}")

    def ubah_gaji(self, gaji_baru):
        if gaji_baru > 0:
            self.__gaji = gaji_baru
        else:
            print("Gaji harus lebih dari 0!")

# Membuat objek
karyawan1 = Karyawan("Imam", 5000000)

# Mengakses atribut publik
print(karyawan1.nama)  # Output: Andi

# Mengakses atribut private (akan error)
# print(karyawan1.__gaji)  # AttributeError

# Menggunakan metode untuk mendapatkan informasi
karyawan1.tampilkan_info()  

# Mengubah gaji dengan metode setter
karyawan1.ubah_gaji(6000000)
karyawan1.tampilkan_info()  
