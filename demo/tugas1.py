# Pure functions for data manipulation
def register_user(nim, password, users, profiles, friends):
    if nim in users:
        return (False, "NIM sudah terdaftar. Silakan login.", users, profiles, friends)
    # Register user
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

# Input/output operations
def register(users, profiles, friends):
    nim = input("Masukkan NIM: ")
    password = input("Masukkan password: ")

    success, message, users, profiles, friends = register_user(nim, password, users, profiles, friends)
    print(message)

    if success:
        skip = input("Ingin mengisi biodata sekarang? (y/n): ")
        if skip.lower() == 'y':
            name = input("Masukkan nama: ")
            age = input("Masukkan umur: ")
            address = input("Masukkan alamat: ")
            profiles = update_profile_data(nim, name, age, address, profiles)
            print("Profil berhasil diperbarui.")

    return users, profiles, friends

def login(users):
    nim = input("Masukkan NIM: ")
    password = input("Masukkan password: ")
    success, message = login_user(nim, password, users)
    print(message)
    return success, nim

def user_menu(nim, users, profiles, friends):
    while True:
        print("\nMenu User:")
        print("1. Lihat Profil")
        print("2. Edit Profil")
        print("3. Tambah Teman")
        print("4. Hapus Teman")
        print("5. Logout")
        choice = input("Pilih menu: ")

        if choice == "1":
            view_profile(nim, profiles, friends)
        elif choice == "2":
            name = input("Masukkan nama: ")
            age = input("Masukkan umur: ")
            address = input("Masukkan alamat: ")
            profiles = update_profile_data(nim, name, age, address, profiles)
            print("Profil berhasil diperbarui.")
        elif choice == "3":
            friend_nim = input("Masukkan NIM teman yang ingin ditambahkan: ")
            success, message, friends = add_friend_data(nim, friend_nim, users, friends)
            print(message)
        elif choice == "4":
            friend_nim = input("Masukkan NIM teman yang ingin dihapus: ")
            success, message, friends = remove_friend_data(nim, friend_nim, friends)
            print(message)
        elif choice == "5":
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid.")

def view_profile(nim, profiles, friends):
    profile = profiles.get(nim, {})
    if profile:
        print(f"\nProfil {nim}:")
        for key, value in profile.items():
            print(f"{key.capitalize()}: {value}")
        print(f"Daftar Teman: {', '.join(friends[nim]) if friends[nim] else 'Belum ada teman.'}")
    else:
        print("\nProfil belum diisi.")

# Main function
def main():
    users = {}  # {nim: password}
    profiles = {}  # {nim: {name: str, age: int, address: str}}
    friends = {}  # {nim: [list of friends]}

    while True:
        print("\nMenu Utama:")
        print("1. Register")
        print("2. Login")
        print("3. Keluar")
        choice = input("Pilih menu: ")

        if choice == "1":
            users, profiles, friends = register(users, profiles, friends)
        elif choice == "2":
            success, nim = login(users)
            if success:
                user_menu(nim, users, profiles, friends)
        elif choice == "3":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
