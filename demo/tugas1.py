from functools import reduce, wraps

# Decorator untuk logging
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Memanggil fungsi '{func.__name__}' dengan argumen {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Hasil dari '{func.__name__}': {result}\n")
        return result
    return wrapper

# HoF dan closure
def age_filter(min_age):
    def filter_profiles(profiles):
        return {nim: data for nim, data in profiles.items() if data["age"] > min_age}
    return filter_profiles

# Decorator
@logger
def register_user(nim, password, users, profiles, friends):
    if nim in users:
        return False, "NIM sudah terdaftar. Silakan login."
    users[nim] = password
    profiles[nim] = {}
    friends[nim] = []
    return True, "Registrasi berhasil."


def login_user(nim, password, users):
    return users.get(nim) == password


@logger
def calculate_total_age(profiles):
    return reduce(lambda acc, data: acc + data["age"], profiles.values(), 0)

@logger
def filter_profiles_by_age(profiles, min_age):
    filter_func = age_filter(min_age)
    return filter_func(profiles)

def main():
    # Data awal
    users = {
        "NIM080": "pass1",
        "NIM095": "pass2",
        "NIM076": "pass3",
        "NIM088": "pass4",
        "NIM106": "pass5"
    }
    profiles = {
        "NIM080": {"name": "Nanda", "age": 21, "address": "Batu"},
        "NIM095": {"name": "Alfi", "age": 20, "address": "Tirto"},
        "NIM076": {"name": "Tegar", "age": 21, "address": "Tirto"},
        "NIM088": {"name": "Dimas", "age": 21, "address": "Batu"},
        "NIM106": {"name": "Farlan", "age": 21, "address": "Tegalgondo"}
    }
    friends = {
        "NIM080": ["NIM095", "NIM076"],
        "NIM095": ["NIM080", "NIM088"],
        "NIM076": ["NIM080"],
        "NIM088": ["NIM095", "NIM106"],
        "NIM106": ["NIM088"]
    }

    # Registrasi pengguna baru
    print("\nRegistrasi pengguna baru:")
    result, message = register_user("NIM080", "newpass", users, profiles, friends)
    print(message)  # Output hasil registrasi


    # Login otomatis
    print("Login otomatis pengguna:")
    for nim, password in users.items():
        success = login_user(nim, password, users)
        print(f"{nim} - {'Login berhasil' if success else 'Login gagal'}")


    # Filter profil berdasarkan usia
    print("\nFilter profil usia > 20:")
    filtered_profiles = filter_profiles_by_age(profiles, 20)
    for nim, data in filtered_profiles.items():
        print(f"{nim}: {data}")

    # Hitung total usia
    print("\nTotal usia semua profil:")
    total_age = calculate_total_age(profiles)
    print(f"Total usia: {total_age}")

if __name__ == "__main__":
    main()
