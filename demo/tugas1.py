from functools import reduce


a = 2       
d = 3       
r = 2       
n = 10      

# Fungsi untuk menghitung elemen aritmetika
def hitung_aritmetika(i):
    return a + i * d

# Fungsi untuk menghitung elemen geometri
def hitung_geometri(i):
    return a * (r ** i)

# Membuat baris aritmetika menggunakan map dan list comprehension
baris_aritmetika = list(map(hitung_aritmetika, [i for i in range(n)]))

# Membuat baris geometri menggunakan map dan list comprehension
baris_geometri = list(map(hitung_geometri, [i for i in range(n)]))

# Menggunakan reduce untuk menghitung total deret
def penjumlahan(x, y):
    return x + y

# Total deret aritmetika
total_aritmetika = reduce(penjumlahan, baris_aritmetika)

# Total deret geometri
total_geometri = reduce(penjumlahan, baris_geometri)

# Output
print("Baris Aritmetika:", baris_aritmetika)
print("Total Deret Aritmetika:", total_aritmetika)
print("Baris Geometri:", baris_geometri)
print("Total Deret Geometri:", total_geometri)
