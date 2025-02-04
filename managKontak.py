class Kontak:
    def __init__(self, nama, nomor_telepon, email):
        self.nama = nama
        self.nomor_telepon = nomor_telepon
        self.email = email

    def info(self):
        return f"{self.nama} ({self.nomor_telepon}, {self.email})"

class DaftarKontak:
    def __init__(self):
        self.daftar_kontak = []

    def tambah_kontak(self, kontak):
        self.daftar_kontak.append(kontak)
        print("Kontak berhasil ditambahkan.")

    def cari_kontak(self, nama):
        for kontak in self.daftar_kontak:
            if kontak.nama.lower() == nama.lower():
                return kontak
        return None

    def hapus_kontak(self, nama):
        kontak = self.cari_kontak(nama)
        if kontak:
            self.daftar_kontak.remove(kontak)
            print(f"Kontak \"{nama}\" berhasil dihapus.")
        else:
            print(f"Kontak \"{nama}\" tidak ditemukan.")

    def tampilkan_daftar(self):
        print("Daftar Kontak:")
        for i, kontak in enumerate(self.daftar_kontak, 1):
            print(f"{i}. {kontak.info()}")

def main():
    daftar_kontak = DaftarKontak()

    while True:
        print("\nSelamat datang di Sistem Pengelolaan Kontak!")
        print("Pilih operasi:")
        print("1. Tambah Kontak Baru")
        print("2. Cari Kontak")
        print("3. Hapus Kontak")
        print("4. Lihat Daftar Kontak")
        print("5. Keluar")

        pilihan = input("Pilih [1-5]: ")

        if pilihan == "1":
            nama = input("Nama: ")
            nomor_telepon = input("Nomor Telepon: ")
            email = input("Email: ")
            kontak_baru = Kontak(nama, nomor_telepon, email)
            daftar_kontak.tambah_kontak(kontak_baru)
        elif pilihan == "2":
            nama_cari = input("Masukkan nama yang ingin dicari: ")
            kontak = daftar_kontak.cari_kontak(nama_cari)
            if kontak:
                print(kontak.info())
            else:
                print(f"Kontak \"{nama_cari}\" tidak ditemukan.")
        elif pilihan == "3":
            nama_hapus = input("Masukkan nama kontak yang ingin dihapus: ")
            daftar_kontak.hapus_kontak(nama_hapus)
        elif pilihan == "4":
            daftar_kontak.tampilkan_daftar()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan Sistem Pengelolaan Kontak!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()