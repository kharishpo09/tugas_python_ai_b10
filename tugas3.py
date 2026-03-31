# 1. Deklarasi Variabel
nama = "Kharis" # string
umur = 21 # integer
versi_python = 3.10 # float
ikut_studi_independen = True # boolean
hobi = ["Membaca", "Coding", "Nonton Film", "Jalan-jalan", "Mendengarkan Musik"] # list

# 2. Manipulasi String
teks_awal = "Halo, perkenalkan aku "
kalimat_lengkap = teks_awal + nama
print(kalimat_lengkap)

print("Panjang karakter namaku:", len(nama))
print("Nama huruf besar:", nama.upper())
print("Nama huruf kecil:", nama.lower())
print() 

# 3. Operasi Matematika
x = 20
y = 6

print("Hasil x + y =", x + y)
print("Hasil x - y =", x - y)
print("Hasil x * y =", x * y)
print("Hasil x / y =", x / y)
print("Hasil pembagian bulat x // y =", x // y)
print("Sisa bagi x % y =", x % y)
print()

# 4. List dan Akses Elemen
proyek_tim = ["Home Cycle", "Web AI", "Data Analyst", "Mobile App", "UI/UX"]
print("List awal proyek:", proyek_tim)

# nampilin elemen pertama (index 0)
print("Proyek utama:", proyek_tim[0])

# nambahin proyek baru ke list
proyek_tim.append("Chatbot")
print("Setelah ditambah:", proyek_tim)

# hapus salah satu item
proyek_tim.remove("UI/UX")
print("Setelah dihapus:", proyek_tim)
print()

# 5. Input User
nama_user = input("Masukkan nama: ")
umur_user = input("Masukkan umur: ")

# cetak hasil input
print("Halo, nama saya " + nama_user + " dan umur saya " + umur_user + " tahun.")