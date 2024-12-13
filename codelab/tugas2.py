import pandas as pd

# Dictionary dari data profil
profiles = {
    "NIM080": {"name": "Nanda", "age": 21, "address": "Batu"},
    "NIM095": {"name": "Alfi", "age": 20, "address": "Tirto"},
    "NIM076": {"name": "Tegar", "age": 21, "address": "Tirto"},
    "NIM088": {"name": "Dimas", "age": 21, "address": "Batu"},
    "NIM106": {"name": "Farlan", "age": 21, "address": "Tegalgondo"}
}

# Mengubah dictionary menjadi Series berdasarkan umur
ages_series = pd.Series({nim: profile["age"] for nim, profile in profiles.items()})
print("Series berdasarkan umur:")
print(ages_series)




