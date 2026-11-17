print("===== BELI TIKET BIOSKOP =====")


# input nama pelanggan
nama = input("Masukkan nama pembeli: ")
print("nama pembeli: " , nama)


# INPUT JENIS TIKET DAN JUMLAH TIKET
jenis = input("Masukkan jenis tiket (VIP/Reguler): ")
jumlah = int(input("Masukkan jumlah tiket: "))
print("Jenis tiket: " , jenis)
print("Jumlah tiket: " , jumlah)

# MENENTUKAN HARGA TIKET

if jenis == "REGULER":
    harga = 35000
elif jenis == "VIP":
    harga = 50000
else:
    harga = 0
    print("Jenis tiket tidak trsedia")

    print("Harga tiket: Rp", harga)

# NGECEK DISKON

total = harga * jumlah

if jumlah > 3:
    diskon = total * 0.1
    total -= diskon
else:
    diskon = 0

total_bayar = total - diskon
print("Total bayar: Rp", total_bayar)
print("Diskon: Rp", diskon)
print("Total pembayaran: Rp", total_bayar)

# PERULANGAN/WHILE

ulang = input("Apakah ingin memesan lagi? (ya/tidak): ")

while ulang == "ya":
    jenis = input("Masukkan jenis tiket (VIP/Reguler): ")
    jumlah = int(input("Masukkan jumlah tiket: "))
    print("Jenis tiket: " , jenis)
    print("Jumlah tiket: " , jumlah)

    if jenis == "REGULER":
        harga = 35000
    elif jenis == "VIP":
        harga = 50000
    else:
        harga = 0
        print("Jenis tiket tidak tersedia")

    total = harga * jumlah

    if jumlah > 3:
        diskon = total * 0.1
        total -= diskon
    else:
        diskon = 0

    total_bayar = total - diskon
    print("Total bayar: Rp", total_bayar)
    print("Diskon: Rp", diskon)
    print("Total pembayaran: Rp", total_bayar)

    ulang = input("Apakah ingin memesan lagi? (ya/tidak): ")

    print("\n===== STRUK PEMESANAN =====")
print("Nama pelanggan :", nama)
print("Jenis tiket    :", jenis)
print("Jumlah tiket   :", jumlah)
print("Harga tiket    : Rp", harga)
print("Total harga    : Rp", total)
print("Diskon         : Rp", diskon)
print("Total bayar    : Rp", total_bayar)
print("===========================")