class Burung:
    def bersuara(self):
        return "Cuit cuit!"

class Kucing:
    def bersuara(self):
        return "Meong!"

# Fungsi yang bisa bekerja dengan berbagai class
def buat_suara(hewan):
    print(hewan.bersuara())

# Membuat objek dari masing-masing class
burung = Burung()
kucing = Kucing()

# Memanggil fungsi yang sama dengan objek berbeda
buat_suara(burung)  
buat_suara(kucing)   
