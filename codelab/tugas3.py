# TO-DO 1: Menerima input tanggal lahir
tanggal_lahir = int(input("Masukkan tanggal lahir (1-31): "))  # Memastikan input adalah angka

# TO-DO 2: Membuat generator expression
generator_kelipatan = (x for x in range(tanggal_lahir, 1000, tanggal_lahir))  # Kelipatan tanggal lahir

# TO-DO 3: Mencetak hasil
print("10 data pertama:")
print(list(generator_kelipatan)[:10])  # Casting list dan slicing untuk mengambil 10 data pertama
