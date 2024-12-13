import pandas as pd

# Dictionary dari data profil
profiles = {
    "NIM080": {"name": "Nanda", "age": 21, "address": "Batu"},
    "NIM095": {"name": "Alfi", "age": 20, "address": "Tirto"},
    "NIM076": {"name": "Tegar", "age": 21, "address": "Tirto"},
    "NIM088": {"name": "Dimas", "age": 21, "address": "Batu"},
    "NIM106": {"name": "Farlan", "age": 21, "address": "Tegalgondo"}
}

# Membuat DataFrame dari dictionary
profiles_df = pd.DataFrame.from_dict(profiles, orient='index')

# Menambahkan kolom index sebagai NIM
profiles_df.index.name = 'NIM'

# Menampilkan DataFrame
print("DataFrame hasil dari dictionary:")
print(profiles_df)
