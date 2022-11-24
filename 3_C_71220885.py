daftar = str(input("Masukkan daftar pesanan : "))
daftar.title()
pesan = daftar.split(',')
print("Daftar pesanan : ",pesan)
tambah = str(input("Masukkan pesanan yang ingin ditambahkan : "))
if tambah in daftar:
    print(tambah.upper(),"sudah berada dalam daftar pesanan.")
else:
    pesan.append(tambah)
    print("Hasil penambahan pada daftar pesanan : ",pesan)
