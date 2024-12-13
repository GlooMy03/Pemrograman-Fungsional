profiles = [
        ("076","Tegar",21,"Tirto"),
        ("080","Nanda",21,"Batu"),
        ("082","Ali",20,"Kalimantan"),
        ("084","Ichsan",21,"Kalimantan"),
        ("088","Dimas",21,"Batu"),
        ("091","Indra",20,"Kalimantan"),
        ("094","Adit",21,"Kalimantan"),
        ("095","Alfi",20,"Tirto"),
        ("104","Zeedan",20,"Tegalgondo"),
        ("106","Farlan",21,"Tegalgondo")
]

nim = [item[0] for item in profiles]
nama_mahasiswa = [item[1] for item in profiles]
umur = [item[2] for item in profiles]
alamat = [item[3] for item in profiles]

import matplotlib.pyplot as plt

garis_x = nim
garis_y = umur

plt.scatter(garis_x, garis_y)
plt.show()

import matplotlib.pyplot as plt

garis_x = nim
garis_y = umur

plt.scatter(garis_x, garis_y)
plt.show()

import matplotlib.pyplot as plt

# Menghitung jumlah mahasiswa per lokasi
locations = {}
for profile in profiles:
    lokasi = profile[3]
    locations[lokasi] = locations.get(lokasi, 0) + 1

# Data untuk pie chart
labels = list(locations.keys())
sizes = list(locations.values())

# Menentukan explode untuk lokasi "Kalimantan"
explode = [0.1 if label == "Kalimantan" else 0 for label in labels]

# Membuat pie chart
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, explode=explode, shadow=True, autopct='%1.1f%%')
plt.title("Distribusi Lokasi Mahasiswa")
plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Membuat figure
plt.figure(figsize=(16, 8))

# Subplot 1: Line Plot
plt.subplot(1, 3, 1)
plt.title("Line Plot")
plt.plot(nim, umur, marker='o', linestyle='-', color='b')
plt.xlabel("NIM")
plt.ylabel("Umur")

# Subplot 2: Pie Chart
plt.subplot(1, 3, 2)
plt.title("Pie Chart")
plt.pie(sizes, labels=labels, explode=explode, shadow=True, autopct='%1.1f%%')

# Subplot 3: Scatter Plot
plt.subplot(1, 3, 3)
plt.title("Scatter Plot")
plt.scatter(nama_mahasiswa, umur, color='r', edgecolors='k')
plt.xlabel("nama mahasiswa")
plt.ylabel("Umur")

# Tampilkan grafik
plt.tight_layout()
plt.show()