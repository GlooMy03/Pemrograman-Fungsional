from functools import reduce

nilai_mahasiswa = {
    'Zaidun' : 99,
    'Suwarsono' : 100,
    'Dedi' : 75,
    'Joko' : 40,
    'Rusdi' : 78,
    'Diki' : 100,
    'Ansori' : 92,
    'Andri' : 76,
    'Kahfi' : 58,
    'Edi' : 77,
    'Dimas' : 15,
    'Sutadi' : 90,
    'Made' : 55,
    'Nyoto' : 88,
    'Widodo' : 100
}

# Hitung total nilai dengan reduce
total_nilai = reduce(lambda x, y: x + y, nilai_mahasiswa.values())

# Dapatkan nilai tertinggi
nilai_tertinggi = reduce(lambda x, y: x if x > y else y, nilai_mahasiswa.values())

# Mahasiswa yang lulus KKM 75
mahasiswa_lulus = list(filter(lambda x: nilai_mahasiswa[x] >= 75, nilai_mahasiswa))

# Tambahkan 5 poin untuk mahasiswa dengan nilai di bawah 75
nilai_mahasiswa_update = dict(
    map(lambda x: (x[0], x[1] + 5) if x[1] < 75 else x, nilai_mahasiswa.items())
)

# Tampilkan hasil
print("Total Nilai:", total_nilai)
print("Nilai Tertinggi:", nilai_tertinggi)
print("Mahasiswa Lulus:", mahasiswa_lulus)
print("Nilai Mahasiswa Update:", nilai_mahasiswa_update)
