data_matkul = [
    ("Fungsional", 87.5, 48),
    ("Jarkom", 91, 52),
    ("Mobile", 79.7, 40),
    ("Pirdas", 92.5, 49),
    ("Web", 89, 55)
]

nama_matkul = [item[0] for item in data_matkul]
nilai = [item[1] for item in data_matkul]
jumlah_mahasiswa = [item[2] for item in data_matkul]

total_nilai = list(map(lambda item: item[1] * item[2], data_matkul))

print("Nama Mata Kuliah:", nama_matkul)
print("Nilai Rata-rata:", nilai)
print("Jumlah Mahasiswa:", jumlah_mahasiswa)
print("Total Nilai:", total_nilai)

#scatter
import matplotlib.pyplot as plt

garis_x = jumlah_mahasiswa
garis_y = nilai

plt.scatter(garis_x, garis_y)
plt.show()

#bar
import matplotlib.pyplot as plt

garis_x = nama_matkul
garis_y = nilai

plt.bar(garis_x, garis_y)
plt.show()

#plot
import matplotlib.pyplot as plt

garis_x = nama_matkul
garis_y = nilai

plt.plot(garis_x, garis_y)
plt.show()

#pie chart
import matplotlib.pyplot as plt

min_index = jumlah_mahasiswa.index(min(jumlah_mahasiswa))
garis_x = nama_matkul
garis_y = jumlah_mahasiswa
explode = [0.1 if i == min_index else 0 for i in range(len(jumlah_mahasiswa))]

plt.pie(garis_y, labels=garis_x, explode=explode, shadow=True)
plt.show()

#all
import matplotlib.pyplot as plt

# Data mata kuliah
data_matkul = [
    ("Fungsional", 87.5, 48),
    ("Jarkom", 91, 52),
    ("Mobile", 79.7, 40),
    ("Pirdas", 92.5, 49),
    ("Web", 89, 55)
]

# Ekstraksi data
nama_matkul = [item[0] for item in data_matkul]
nilai = [item[1] for item in data_matkul]
jumlah_mahasiswa = [item[2] for item in data_matkul]
total_nilai = [round(item[1] * item[2], 2) for item in data_matkul]


# Tentukan indeks data terkecil untuk di-explode (pie chart)
min_index = jumlah_mahasiswa.index(min(jumlah_mahasiswa))
explode = [0.1 if i == min_index else 0 for i in range(len(jumlah_mahasiswa))]

# Membuat subplot dengan 2 baris dan 2 kolom
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Scatter plot
axs[0, 0].scatter(jumlah_mahasiswa, nilai, color='blue', s=100, edgecolor='black')
axs[0, 0].set_title('Scatter Plot: Rata-rata Nilai vs Jumlah Mahasiswa')
axs[0, 0].set_xlabel('Jumlah Mahasiswa')
axs[0, 0].set_ylabel('Rata-rata Nilai')

# Diagram Batang (Total Nilai)
axs[0, 1].bar(nama_matkul, total_nilai, color='green', edgecolor='black')
axs[0, 1].set_title('Diagram Batang: Total Nilai')
axs[0, 1].set_xlabel('Mata Kuliah')
axs[0, 1].set_ylabel('Total Nilai')

# Diagram Garis (Rata-rata Nilai)
axs[1, 0].plot(nama_matkul, nilai, marker='o', color='blue', linestyle='-')
axs[1, 0].set_title('Diagram Garis: Rata-rata Nilai')
axs[1, 0].set_xlabel('Mata Kuliah')
axs[1, 0].set_ylabel('Rata-rata Nilai')
axs[1, 0].grid(alpha=0.3)

# Pie chart (Jumlah Mahasiswa)
axs[1, 1].pie(jumlah_mahasiswa, labels=nama_matkul, autopct='%1.1f%%', startangle=90, explode=explode, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
axs[1, 1].set_title('Pie Chart: Distribusi Jumlah Mahasiswa')

# Penyesuaian layout agar tidak saling tumpang tindih
plt.tight_layout()

# Tampilkan plot
plt.show()




