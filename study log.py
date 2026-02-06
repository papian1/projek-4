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
    # Mengecek apakah ada catatan atau tidak
    if len(catatan) == 0:
        print("\n⚠ Belum ada catatan belajar. Mulai tambah catatan sekarang!\n")
        return
    
    # Menampilkan semua catatan dengan format rapi
    print("\n" + "="*60)
    print("📚 DAFTAR CATATAN BELAJAR")
    print("="*60)
    
    for i, item in enumerate(catatan, start=1):
        print(f"\n{i}. Mata Pelajaran: {item['mapel']}")
        print(f"   Topik: {item['topik']}")
        print(f"   Durasi: {item['durasi']} menit")
    
    print("\n" + "="*60 + "\n")

def total_waktu():
    # Mengecek apakah ada catatan atau tidak
    if len(catatan) == 0:
        print("\n⚠ Belum ada catatan belajar. Mulai tambah catatan sekarang!\n")
        return
    
    # Menghitung total durasi dari semua catatan
    jumlah_total = 0
    for item in catatan:
        jumlah_total += item['durasi']
    
    # Menampilkan hasil dengan format rapi
    print("\n" + "="*60)
    print("⏱ TOTAL WAKTU BELAJAR")
    print("="*60)
    print(f"\nJumlah catatan: {len(catatan)}")
    print(f"Total durasi: {jumlah_total} menit")
    
    # Konversi ke jam dan menit untuk lebih mudah dibaca
    jam = jumlah_total // 60
    menit = jumlah_total % 60
    print(f"Setara dengan: {jam} jam {menit} menit")
    print("\n" + "="*60 + "\n")

def mapel_favorit():
    # Mengecek apakah ada catatan atau tidak
    if len(catatan) == 0:
        print("\n⚠ Belum ada catatan belajar. Mulai tambah catatan sekarang!\n")
        return
    
    # Menghitung total durasi untuk setiap mapel
    statistik_mapel = {}
    for item in catatan:
        mapel = item['mapel']
        durasi = item['durasi']
        
        # Jika mapel sudah ada, tambah durasinya
        if mapel in statistik_mapel:
            statistik_mapel[mapel] += durasi
        else:
            # Jika mapel baru, buat entry baru
            statistik_mapel[mapel] = durasi
    
    # Mengurutkan mapel berdasarkan total durasi (terbesar ke terkecil)
    mapel_terurut = sorted(statistik_mapel.items(), key=lambda x: x[1], reverse=True)
    
    # Menampilkan hasil dengan format rapi
    print("\n" + "="*60)
    print("⭐ MATA PELAJARAN FAVORIT (Berdasarkan Total Waktu Belajar)")
    print("="*60)
    
    for i, (mapel, total_durasi) in enumerate(mapel_terurut, start=1):
        jam = total_durasi // 60
        menit = total_durasi % 60
        print(f"\n{i}. {mapel}")
        print(f"   Total waktu: {total_durasi} menit ({jam}j {menit}m)")
    
    # Menampilkan mapel favorit (dengan waktu belajar terbanyak)
    mapel_teratas = mapel_terurut[0][0]
    print(f"\n🏆 Mapel Favorit Anda: {mapel_teratas}")
    print("="*60 + "\n")

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Mata pelajaran favorit")
    print("5. Keluar")

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
        mapel_favorit()
    elif pilihan == "5":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")