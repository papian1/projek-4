catatan = []

def tambah_catatan():
    # Meminta input dari pengguna
    mapel = input("Masukkan mata pelajaran: ")
    topik = input("Masukkan topik belajar: ")
    
    # Validasi durasi agar hanya angka
    while True:
        try:
            durasi = int(input("Masukkan durasi belajar (menit): "))
            if durasi > 0:
                break
            else:
                print("Durasi harus lebih dari 0!")
        except ValueError:
            print("Masukkan angka yang valid!")
    
    # Membuat catatan dalam bentuk dictionary (kamus)
    catatan_baru = {
        "mapel": mapel,
        "topik": topik,
        "durasi": durasi
    }
    
    # Menambahkan catatan ke dalam list
    catatan.append(catatan_baru)
    print(f"\n✓ Catatan '{topik}' berhasil ditambahkan!\n")

def lihat_catatan():
    pass

def total_waktu():
    pass

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "4":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")