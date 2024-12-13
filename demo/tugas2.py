import pandas as pd

# Membaca file CSV. Sesuaikan dengan nama file yang diimpor
data = pd.read_csv('Dataset Harga Buah dan Sayur.csv')

print(data.head(10))    

data.info()

average_price_per_year = data.groupby(['date', 'item'])['price'].mean()

# Menampilkan hasil
print(average_price_per_year)

# Menemukan harga tertinggi dan terendah
max_price = data['price'].max()
min_price = data['price'].min()

# Menemukan produk dengan harga tertinggi
product_max_price = data[data['price'] == max_price]

# Menemukan produk dengan harga terendah
product_min_price = data[data['price'] == min_price]

# Menampilkan hasil
print("Produk dengan harga tertinggi:")
print(product_max_price)

print("\nProduk dengan harga terendah:")
print(product_min_price)

# Filter produk dengan harga antara 1.50 hingga 2.35
filtered_products = data[(data['price'] >= 1.50) & (data['price'] <= 2.35)]

# Menampilkan hasil
print("Produk dengan harga antara 1.50 sampai 2.35:")
print(filtered_products)