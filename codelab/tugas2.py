books = [
    {'judul':'Pulang', 'penulis': 'Tere Liye', 'halaman': 400},
    {'judul':'Kapan Nanti', 'penulis': 'Ziggy Z.', 'halaman': 142},
    {'judul':'Namaku Alam', 'penulis': 'Leila S. Chudori', 'halaman': 448},
    {'judul':'Origin', 'penulis': 'Dan Brown', 'halaman': 511},
    {'judul':'Rumah Lebah', 'penulis': 'Ruwi Meita', 'halaman': 288},
    {'judul':'Kubah', 'penulis': 'Ahmad Tohari', 'halaman': 184},
    {'judul':'Dompet Ayah Sepatu Ibu', 'penulis': 'J. S. Khairen', 'halaman': 210},
]

# TODO 1: Gunakan list comprehension untuk menyaring buku dari books yang judulnya diawali dengan huruf 'K'.
filtered_books = [book for book in books if book['judul'].startswith('K')]

# TODO 2: Cetak hasil buku yang tersaring
print("Buku yang judulnya diawali huruf 'K':")

# TODO 3: Gunakan loop untuk iterasi setiap buku di filtered_books.
for book in filtered_books:
# TODO 4: Di dalam loop, cetak detail buku berupa judul, penulis, dan halaman.
    print(f"Judul: {book['judul']}, Penulis: {book['penulis']}, Halaman: {book['halaman']}")


# TODO 1: Definisikan fungsi untuk mendapatkan judul buku
def judul_buku(book):
    # TODO 2: Mengembalikan judul buku dari dictionary 'book'
    return book['judul']

# TODO 3: Gunakan `map` untuk mendapatkan semua judul buku
judul_buku_list = map(judul_buku, books)

# TODO 4: Cetak judul buku dan gunakan loop untuk iterasi melalui hasil judul_buku
print("Daftar judul buku:")
for judul in judul_buku_list:
    print(judul)


# TODO 1: Definisikan fungsi untuk memeriksa jumlah halaman
def halaman(book):
    # TODO 2: Mengembalikan True jika halaman buku lebih dari 200
    return book['halaman'] > 200

# TODO 3: Gunakan filter untuk menyaring buku
#books_200 = filter(halaman, books)
books_200 = filter(lambda book: book['halaman'] > 200, books)

# TODO 4: Cetak hasil, gunakan loop untuk iterasi melalui hasil books_200
print("Buku dengan lebih dari 200 halaman:")
for book in books_200:
    print(f"Judul: {book['judul']}, Penulis: {book['penulis']}, Halaman: {book['halaman']}")


# TODO 1: Import modul yang diperlukan
from functools import reduce
# TODO 2: Definisikan fungsi untuk menghitung total halaman
# def hitung_halaman(total, book):
#     # TODO 3: Tambahkan jumlah halaman buku ke total
#     return total + book['halaman']

# # TODO 4: Gunakan reduce untuk menghitung total halaman
# #total_halaman = reduce(hitung_halaman, books, 0)
# print(reduce(hitung_halaman,books,0))
t = reduce(lambda total, book: total + book['halaman'], books, 0)

# TODO 5: Cetak total halaman
print(f"Total jumlah halaman semua buku: {t}")