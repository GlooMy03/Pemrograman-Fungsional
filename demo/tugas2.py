import time

# Dekorator untuk menghitung waktu eksekusi
def hitung_waktu(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Waktu mulai
        result = func(*args, **kwargs)  # Eksekusi fungsi
        end_time = time.time()  # Waktu selesai
        print(f"Waktu eksekusi: {end_time - start_time} detik")
        return result
    return wrapper

# Fungsi untuk menghitung rata-rata nilai mahasiswa
@hitung_waktu
def hitung_rata_rata(nilai_mahasiswa):
    return sum(nilai_mahasiswa) / len(nilai_mahasiswa)

# Fungsi untuk menghitung jumlah nilai yang di atas rata-rata
@hitung_waktu
def hitung_nilai_above(nilai_mahasiswa):
    rata_rata = hitung_rata_rata(nilai_mahasiswa)
    return len(list(filter(lambda x: x > rata_rata, nilai_mahasiswa)))

# Inputan nilai mahasiswa (contoh)
nilai_input = input("Masukkan nilai mahasiswa (pisahkan dengan koma): ")
nilai_mahasiswa = list(map(float, nilai_input.split(',')))

# Menampilkan hasil
print(f"Rata-rata nilai: {hitung_rata_rata(nilai_mahasiswa)}")
print(f"Jumlah nilai yang di atas rata-rata: {hitung_nilai_above(nilai_mahasiswa)}")
