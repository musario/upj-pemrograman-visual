# Case: Diskon barang
# Condition: Jika hari libur dan pembeli berumur 18 hingga 25 maka barang yang dibeli mendapat diskon 30%.

umur_pelanggan = int(input("Masukkan umur Anda: "))
harga_barang = 10000
hari_libur = True
pesan = "Karena bukan hari libur, harga barang tidak mendapat diskon"
diskon = 0

if umur_pelanggan >= 18 and umur_pelanggan <= 25 and hari_libur:
    diskon = harga_barang * 35/100
    harga_barang = int(harga_barang - diskon)
    pesan = "Karena hari libur, harga barang kamu mendapat diskon sebesar 35%"

print(f"Harga yang harus dibayar: Rp{harga_barang}")
print(pesan)
