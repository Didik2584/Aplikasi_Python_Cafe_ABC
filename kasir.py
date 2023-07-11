# Daftar menu kafe
menu = {
    "Nasi Goreng": 15000,
    "Mie Goreng": 12000,
    "Kopi": 5000,
    "Teh": 4000,
    "Es Teh": 6000,
    "Es Kopi": 7000
}

# Inisialisasi pesanan
pesanan = []

# Fungsi untuk menampilkan menu kafe
def tampilkan_menu():
    print("Menu Cafe ABC:")
    for item, harga in menu.items():
        print("- {}: Rp {}".format(item, harga))

# Fungsi untuk menambahkan pesanan
def tambah_pesanan(item):
    if item in menu:
        pesanan.append(item)
        print("{} telah ditambahkan ke pesanan.".format(item))
    else:
        print("Maaf, {} tidak ada di menu.".format(item))

# Fungsi untuk menghitung total biaya pesanan
def hitung_total():
    total = 0
    for item in pesanan:
        total += menu[item]
    return total

# Fungsi untuk menjalankan aplikasi
def jalankan_aplikasi():
    print("Selamat datang di Cafe ABC!")
    tampilkan_menu()

    while True:
        print("\nApa yang ingin Anda lakukan?")
        print("1. Tambahkan pesanan")
        print("2. Lihat pesanan")
        print("3. Hitung total biaya")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == "1":
            item = input("Masukkan item yang ingin dipesan: ")
            tambah_pesanan(item)
        elif pilihan == "2":
            print("Pesanan Anda:")
            for item in pesanan:
                print("- {}".format(item))
        elif pilihan == "3":
            total = hitung_total()
            print("Total biaya pesanan: Rp {}".format(total))
        elif pilihan == "4":
            print("Terima kasih telah menggunakan aplikasi Cafe ABC. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")

# Menjalankan aplikasi
jalankan_aplikasi()
