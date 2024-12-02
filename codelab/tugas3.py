#TO_DO 1
# HANYA CONTOH, silahkan dimodif
nilai_mahasiswa = {
    "example": {"example1": 80, "example2": 75, "example3": 85}

}

#TO_DO 2
# Function each average
def average_per_mahasiswa(nilai):
  averages = {}
  for mahasiswa, matkul in nilai.items():
    rata_rata = sum(matkul.values()) / len(matkul)
    averages[mahasiswa] = rata_rata
  return averages



#TO_DO 3
# Function all average
def average_all_mahasiswa(nilai):
  total_nilai = 0
  total_mahasiswa = 0
  for matkul in nilai.values():
    total_nilai += sum(matkul.values())
    total_mahasiswa += len(matkul)

  return total_nilai / total_mahasiswa if total_mahasiswa > 0 else 0

#panggil fungsi dan tampilkan hasilnya

rata_rata_per_mahasiswa = average_per_mahasiswa(nilai_mahasiswa)
rata_rata_semua_mahasiswa = average_all_mahasiswa(nilai_mahasiswa)

print("rata-rata nilai per mahasiswa: ")
for mahasiswa, rata in rata_rata_per_mahasiswa.items():
  print(f"{mahasiswa}: {rata:.2f}")

print(f"\nrata-rata nilai seluruh mahasiswa: {rata_rata_semua_mahasiswa:.2f}")


