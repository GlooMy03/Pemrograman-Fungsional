data_mahasiswa = [
    {'nama': 'Karina', 'matkul': 'Pemrograman Fungsional', 'nilai': 90},
    {'nama': 'Seulgi', 'matkul': 'Pemrograman Mobile', 'nilai': 56},
    {'nama': 'Wonyoung', 'matkul': 'Pemrograman Web', 'nilai': 95},
    {'nama': 'Hanni', 'matkul': 'Piranti Cerdas', 'nilai': 88},
    {'nama': 'Jihyo', 'matkul': 'Jaringan Komputer', 'nilai': 63},
]

#TO-DO 1: deklarasi fungsi
def rata_rata(param):
  #TO-DO 2: proses hitung rata-rata
  total_nilai = sum(item['nilai'] for item in param)  # Menjumlahkan semua nilai
  jumlah_mahasiswa = len(param)  # Menghitung jumlah mahasiswa
  return total_nilai / jumlah_mahasiswa if jumlah_mahasiswa > 0 else 0 #TO-DO 3

#TO-DO 4: panggil fungsi rata_rata() dan tampilkan hasilnya
print("Rata-rata nilai kelima mahasiswa tersebut adalah: ", rata_rata(data_mahasiswa))

#TO-DO 1: deklarasi fungsi
def kelulusan(param):
  #TO-DO 2: buat salinan data baru agar tidak merubah data asli (effect-free)
  data_kelulusan = [item.copy() for item in param]

  #TO_DO 3: ubah data nilai sesuai ketentuan
  for item in data_kelulusan:  # Iterasi data
      if item['nilai'] >= 85:  # Pengecekan kondisi
          item['nilai'] = 'sempurna'  # Change data
      elif item['nilai'] >= 60:  # Pengecekan kondisi
          item['nilai'] = 'memenuhi'  # Change data
      else:
          item['nilai'] = 'gagal'  # Change data

  return data_kelulusan #TO-DO 4: output fungsi

#TO-DO 5: panggil fungsi dan tampilkan hasilnya
print("Data kelulusan mahasiswa = ")
hasil_kelulusan = kelulusan(data_mahasiswa)
for mahasiswa in hasil_kelulusan:
  print(f"Nama: {mahasiswa['nama']}, Matkul: {mahasiswa['matkul']}, Nilai: {mahasiswa['nilai']}")


#TO_DO 1: deklarasi fungsi generator
def nim_genap(param):
  #TO-DO 2: isi fungsi
  for item in param:
        if item['nilai'] % 2 == 0:  # Cek jika nilai genap
            yield item  # TO-DO 3: Output fungsi

#TO_DO 4: panggil fungsi generator untuk membuat generator object yang berisi
         #data mahasiswa dengan nilai ganjil/genap sesuai nim anda
var = nim_genap(data_mahasiswa)

#TO_DO 5: menampilkan/print hasil dari generator object
print("Nilai mahasiswa yang genap:")
for nilai in var:
    print(f"Nama: {nilai['nama']}, Matkul: {nilai['matkul']}, Nilai: {nilai['nilai']}")

