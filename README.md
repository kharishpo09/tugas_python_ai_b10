# 📚 Ringkasan Tugas Python AI

Repository ini berisi kumpulan tugas dasar pemrograman Python yang mencakup berbagai konsep, mulai dari struktur data hingga analisis data dasar.

Berikut adalah kesimpulan pembelajaran dari Tugas 4, Tugas 5, dan Tugas 6:

## 📝 Tugas 4: Struktur Data (Data Structures)
Pada tugas ini, saya mempelajari cara menyimpan dan memanipulasi berbagai jenis data menggunakan struktur bawaan Python:
- **List:** Struktur data fleksibel yang elemennya bisa ditambah, dihapus, dan diiris (*slicing*).
- **Tuple:** Mirip dengan List, namun bersifat *immutable* (tidak bisa diubah setelah dideklarasikan). Sangat berguna untuk *unpacking* variabel.
- **Set:** Struktur data himpunan yang otomatis menghilangkan elemen duplikat, dan mendukung operasi matematika seperti *Union* dan *Intersection*.
- **Dictionary:** Penyimpanan data berbasis *key-value* berpasangan yang memudahkan pencarian data spesifik.
- **Comprehensions:** Teknik menulis kode yang lebih ringkas untuk membuat List, Set, atau Dictionary dari hasil iterasi.

## ⚙️ Tugas 5: Function dan Object-Oriented Programming (OOP)
Pada tugas ini, saya menerapkan konsep modularitas dan pemodelan objek:
- **Function:** Membuat blok kode (seperti `greet`, `tambah`, `rata_rata`) yang bisa dipanggil berulang kali lengkap dengan *Type Hinting* agar tipe data lebih terstruktur.
- **Class & Object:** Menggunakan OOP sederhana dengan membuat Class `Student`. Di dalamnya terdapat atribut nama, nim, nilai, serta *method* untuk menambahkan skor dan mengecek status kelulusan secara otomatis.

## 📊 Tugas 6: Data Analysis Dasar & File I/O
Tugas terakhir ini mensimulasikan penerapan Python untuk analisis data mini:
- **NumPy:** Digunakan untuk membuat *array* nilai acak dan menghitung statistik dasar (rata-rata, median, standar deviasi, min, max).
- **Pandas:** Digunakan untuk mengubah data menjadi format tabel berkolom (*DataFrame*), serta menggunakan fungsi *lambda* untuk menentukan status kelulusan.
- **File Input/Output:** Menggunakan metode `with open()` untuk mengekstrak dan menulis laporan perhitungan otomatis ke dalam sebuah file `.txt`.
- **Integrasi OOP:** Membuat Class `GradeBook` yang langsung memproses data dari *DataFrame* untuk menghitung persentase kelulusan dan menyimpan ringkasannya.
