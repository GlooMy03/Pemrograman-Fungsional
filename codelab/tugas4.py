import pandas as pd

# Membaca file CSV. Sesuaikan dengan nama file yang diimpor
data = pd.read_csv('data.csv')

# Menampilkan 5 baris pertama
print(data.head())

data.info()

print(data.describe())