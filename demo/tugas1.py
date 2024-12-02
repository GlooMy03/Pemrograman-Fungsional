# Dictionary untuk menyimpan data user, profile, dan friends list
users = {}  # {nim: password}
profiles = {}  # {nim: {name: str, age: int, address: str}}
friends = {}  # {nim: [list of friends]}


# Fungsi untuk register
def register():
    nim = input("Masukkan NIM: ")
    if nim in users:
        print("NIM sudah terdaftar. Silakan login.")
        return
    password = input("Masukkan password: ")
    users[nim] = password
    print(users)
    profiles[nim] = {}
    friends[nim] = []
    print("Registrasi berhasil.")

    skip = input("Ingin mengisi biodata sekarang? (y/n): ")
    if skip.lower() == 'y':
        update_profile(nim)


# Fungsi untuk login
def login():
    nim = input("Masukkan NIM: ")
    password = input("Masukkan password: ")

    if nim in users and users[nim] == password:
        print("Login berhasil.")
        user_menu(nim)
    else:
        print("NIM atau password salah.")


# Fungsi untuk menampilkan menu user
def user_menu(nim):
    while True:
        print("\nMenu User:")
        print("1. Lihat Profil")
        print("2. Edit Profil")
        print("3. Tambah Teman")
        print("4. Hapus Teman")
        print("5. Logout")
        choice = input("Pilih menu: ")

        if choice == "1":
            view_profile(nim)
        elif choice == "2":
            update_profile(nim)
        elif choice == "3":
            add_friend(nim)
        elif choice == "4":
            remove_friend(nim)
        elif choice == "5":
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid.")


# Fungsi untuk melihat profil
def view_profile(nim):
    profile = profiles.get(nim, {})
    if profile:
        print(f"\nProfil {nim}:")
        for key, value in profile.items():
            print(f"{key.capitalize()}: {value}")
        print(f"Daftar Teman: {', '.join(friends[nim]) if friends[nim] else 'Belum ada teman.'}")
    else:
        print("\nProfil belum diisi.")


# Fungsi untuk memperbarui profil
def update_profile(nim):
    name = input("Masukkan nama: ")
    age = input("Masukkan umur: ")
    address = input("Masukkan alamat: ")

    profiles[nim] = {"name": name, "age": age, "address": address}
    print("Profil berhasil diperbarui.")


# Fungsi untuk menambahkan teman
def add_friend(nim):
    friend_nim = input("Masukkan NIM teman yang ingin ditambahkan: ")
    if friend_nim in users and friend_nim != nim:
        friends[nim].append(friend_nim)
        print(f"Teman dengan NIM {friend_nim} berhasil ditambahkan.")
    else:
        print("NIM teman tidak valid.")


# Fungsi untuk menghapus teman
def remove_friend(nim):
    friend_nim = input("Masukkan NIM teman yang ingin dihapus: ")
    if friend_nim in friends[nim]:
        friends[nim].remove(friend_nim)
        print(f"Teman dengan NIM {friend_nim} berhasil dihapus.")
    else:
        print("NIM teman tidak ada dalam daftar teman.")


# Fungsi utama
def main():
    while True:
        print("\nMenu Utama:")
        print("1. Register")
        print("2. Login")
        print("3. Keluar")
        choice = input("Pilih menu: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
