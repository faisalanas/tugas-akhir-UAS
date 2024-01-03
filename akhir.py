# Dictionary produk dan harganya
produk_harga = {
    'daging sapi' : 90000 ,
    'telur ayam' : 30000 ,
    'daging ayam' : 40000 ,
    'roti tawar' : 10000 ,
    'beras' :11000 ,
    'air minum' :3000 ,
    'minyak goreng' : 24000 ,
    'gula' : 12000 ,
    }
print("***Selamat datang di arsamart***")

# Fungsi untuk menampilkan daftar produk
def tampilkan_produk():
    print("Daftar Produk:")
    for produk, harga in produk_harga.items():
        print(f"{produk}: Rp{harga}")

# Fungsi untuk menghitung total harga belanjaan
def hitung_total(belanjaan):
    total = 0
    for item in belanjaan:
        if item in produk_harga:
            total += produk_harga[item]
        else:
            print(f"Produk '{item}' tidak ditemukan.")
    return total

# Fungsi utama program
def kasir_supermarket():
    belanjaan = []
    while True:
        tampilkan_produk()
        print("Pilih produk yang ingin dibeli atau ketik 'selesai' untuk selesai belanja.")
        produk = input("Masukkan nama produk: ").lower()

        if produk == 'selesai':
            break
        elif produk in produk_harga:
            belanjaan.append(produk)
        else:
            print("Produk tidak valid.")

    # Hitung total belanjaan
    total_harga = hitung_total(belanjaan)

    # Tampilkan struk dan total belanjaan
    print("\n--- Struk Belanja ---")
    for item in belanjaan:
        print(f"{item}: Rp{produk_harga[item]}")
    print(f"Total: Rp{total_harga}")

# Panggil fungsi utama kasir
kasir_supermarket()
#Ucapanterimakasih
print ("\nTerimakasih atas kunjungan Anda")
