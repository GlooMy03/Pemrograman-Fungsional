from functools import reduce

def register_user(nim, password, users, profiles, friends):
    if nim in users:
        return (False, "NIM sudah terdaftar. Silakan login.", users, profiles, friends)
    users[nim] = password
    profiles[nim] = {}
    friends[nim] = []
    return (True, "Registrasi berhasil.", users, profiles, friends)

def update_profile_data(nim, name, age, address, profiles):
    profiles[nim] = {"name": name, "age": age, "address": address}
    return profiles

def add_friend_data(nim, friend_nim, users, friends):
    if friend_nim in users and friend_nim != nim:
        friends[nim].append(friend_nim)
        return (True, f"Teman dengan NIM {friend_nim} berhasil ditambahkan.", friends)
    else:
        return (False, "NIM teman tidak valid.", friends)

def remove_friend_data(nim, friend_nim, friends):
    if friend_nim in friends[nim]:
        friends[nim].remove(friend_nim)
        return (True, f"Teman dengan NIM {friend_nim} berhasil dihapus.", friends)
    else:
        return (False, "NIM teman tidak ada dalam daftar teman.", friends)

def login_user(nim, password, users):
    if nim in users and users[nim] == password:
        return (True, "Login berhasil.")
    return (False, "NIM atau password salah.")

def view_profile(nim, profiles, friends):
    profile = profiles.get(nim, {})
    if profile:
        print(f"\nProfil {nim}:")
        for key, value in profile.items():
            print(f"{key.capitalize()}: {value}")
    friend_list = friends.get(nim, [])
    if friend_list:
        print("Daftar Teman:")
        for friend in friend_list:
            print(f"- {friend}")
    return (nim, friend_list)


def filter_profile_by_age(profiles, min_age=20):
    filtered_profiles = {nim: data for nim, data in profiles.items() if data["age"] > min_age}
    print("Daftar profil dengan umur di atas 20:")
    for nim, data in filtered_profiles.items():
        print(f"NIM: {nim}, Nama: {data['name']}, Umur: {data['age']}, Alamat: {data['address']}")
    return filtered_profiles


def total_age(profiles):
    def age_sum(acc, data):
        return acc + data["age"]
    total = reduce(age_sum, profiles.values(), 0)
    return total

def main():
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

    print("Login otomatis pengguna:")
    login_results = [(nim, *login_user(nim, password, users)) for nim, password in users.items()]
    for nim, success, message in login_results:
        print(f"{nim} - {message}")
        if success:
            view_profile(nim, profiles, friends)

   
    filter_profile_by_age(profiles, min_age=20)

    
    total = total_age(profiles)
    print(f"\nTotal usia dari semua profil: {total}")

if __name__ == "__main__":
    main()
