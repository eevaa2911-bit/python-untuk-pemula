# Bab 8: Class dan Object

class Siswa:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

    def tampilkan_data(self):
        print("Nama:", self.nama)
        print("Kelas:", self.kelas)

# Membuat object
siswa1 = Siswa("Eva", 11)

# Menampilkan data object
siswa1.tampilkan_data()
