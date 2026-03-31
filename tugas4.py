# --- List ---
print("\n--- Bagian 1: List ---")
data_kampus = ["Informatika", 2024, "Kharis", True, 3.85, "Semester 6"]

print("Elemen pertama:", data_kampus[0])
print("Elemen terakhir:", data_kampus[-1])
print("Slicing [1:5:2]:", data_kampus[1:5:2])

print("List sebelum diubah:", data_kampus)
data_kampus.append("Lulus")
data_kampus.insert(2, "AI Developer")
data_kampus.extend(["Studi Independen", 100])
print("List setelah append, insert, extend:", data_kampus)

data_kampus.pop() 
data_kampus.remove(True) 
print("List setelah pop dan remove:", data_kampus)


# --- Tuple  ---
print("\n--- Bagian 2: Tuple ---")
info_studi = ("Python", "Data Science", "Machine Learning", 6, "Bulan")

print("Panjang tuple:", len(info_studi))
print("Akses indeks ke-2:", info_studi[2])

materi1, materi2, *sisa_info = info_studi
print("Unpacking -> Materi 1:", materi1, "| Materi 2:", materi2, "| Sisa:", sisa_info)


# --- Set ---
print("\n--- Bagian 3: Set ---")
set_a = {1, 2, 3, 3, 4, 5, 5} 
set_b = {4, 5, 6, 7, 8}

print("Set A asli (duplikat otomatis hilang):", set_a)
print("Union (gabungan):", set_a | set_b)
print("Intersection (irisan):", set_a & set_b)
print("Difference (A - B):", set_a - set_b)
print("Symmetric Difference (A ^ B):", set_a ^ set_b)


# --- Dictionary ---
print("\n--- Bagian 4: Dictionary ---")
mhs = {
    "nama": "Kharis",
    "nim": "21009876",
    "angkatan": 2023,
    "kota": "Surabaya"
}

mhs["jurusan"] = "Teknik Informatika" 
mhs["angkatan"] = 2022 
del mhs["kota"] 

print("Keys aja:", mhs.keys())
print("Values aja:", mhs.values())
print("Items (semua):", mhs.items())
print("Iterasi key-value:")
for k, v in mhs.items():
    print(f"- {k}: {v}")


# --- Nested Structures ---
print("\n--- Bagian 5: Nested Structures ---")
daftar_buku = [
    {"judul": "Dasar Pemrograman Python", "penulis": "Budi Raharjo", "tahun": 2019},
    {"judul": "Pengantar Artificial Intelligence", "penulis": "Andi Susanto", "tahun": 2022},
    {"judul": "Machine Learning untuk Pemula", "penulis": "Cici Pertiwi", "tahun": 2021},
    {"judul": "Deep Learning Modern", "penulis": "Dedi Kurniawan", "tahun": 2023}
]

print("Daftar Judul Buku:")
for buku in daftar_buku:
    print(buku["judul"])

buku_baru = [buku["judul"] for buku in daftar_buku if buku["tahun"] >= 2022]
print("Buku terbitan >= 2022:", buku_baru)


# --- Comprehension & Utilitas ---
print("\n--- Bagian 6: Comprehension ---")
angka_genap = [x for x in range(1, 21) if x % 2 == 0]
angka_kuadrat = [x**2 for x in range(1, 21)]
print("List Genap 1-20:", angka_genap)
print("List Kuadrat 1-20:", angka_kuadrat)


cek_angka = {x: "genap" if x % 2 == 0 else "ganjil" for x in range(1, 11)}
print("Dict ganjil genap 1-10:", cek_angka)

kalimat = "belajar ngoding python"
huruf_unik = {huruf.lower() for huruf in kalimat if huruf != ' '}
print("Huruf unik di kalimat:", huruf_unik)


# --- Keanggotaan & Pencarian Sederhana ---
print("\n--- Bagian 7: Keanggotaan & Pencarian ---")
if "Kharis" in data_kampus:
    posisi = data_kampus.index("Kharis")
    print(f"'Kharis' ketemu di list data_kampus pada indeks ke-{posisi}")
else:
    print("'Kharis' nggak ada di list")

print("Apakah huruf 'z' ada di set huruf unik?", 'z' in huruf_unik)
print("Apakah huruf 'o' ada di set huruf unik?", 'o' in huruf_unik)