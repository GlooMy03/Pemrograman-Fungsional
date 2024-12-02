nilai = [ {'matkul': 'Fungsional', 'nilai': 95},
          {'matkul': 'Mobile', 'nilai': 55} ]

def tambah_nilai(nilai, nama_matkul, jumlah_nilai): # TO-DO 1, input fungsi
    nilai_baru = [item.copy() for item in nilai] # TO-DO 3, proses fungsi harus effect-free (tidak boleh mengakses global)
    for item in nilai_baru:
        if item['matkul'] == nama_matkul:
            item['nilai'] += jumlah_nilai
            print(f"Nilai {nama_matkul} ditambahkan {jumlah_nilai}. \nTotal nilai {nama_matkul} saat ini {item['nilai']}")
            break
    else:
        print(f"Mata kuliah {nama_matkul} tidak ditemukan dalam daftar!")
    return nilai_baru # TO-DO 2, fungsi harus memberikan hasil

# Panggil fungsi tambah_nilai
nilai_baru = tambah_nilai(nilai, 'Mobile', 15) # TO-DO 4

# Cek nilai awal
print("Nilai awal: ",nilai)

# Cek nilai hasil tambah_nilai
print("Nilai update: ",nilai_baru)

#sub A
# TO-DO 1: Deklarasi fungsi
def cetak_nilai(param):
    # TO-DO 2: Loop/iterasi data
    for item in param:
        # TO-DO 3: Output fungsi
        yield item  # Menggunakan yield untuk menghasilkan data satu per satu

# Panggil fungsi cetak_nilai
# TO-DO 4
generator_nilai = cetak_nilai(nilai)  # Menghasilkan objek generator

# TO-DO 5: Tampilkan data/print out generator
# Untuk menunjukkan penggunaan next(), kita perlu membuat generator baru
# NIM genap: menggunakan next()
print("Data nilai menggunakan generator (NIM genap):")

try:
    print(next(generator_nilai))  # Mencetak item pertama
    print(next(generator_nilai))  # Mencetak item kedua
except StopIteration:
    print("Semua nilai telah ditampilkan.")