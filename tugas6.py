import os
import numpy as np
import pandas as pd
np.random.seed(42)

class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        return round(self.df['nilai'].mean(), 2)

    def pass_rate(self, threshold: float = 70.0) -> float:
        jumlah_lulus = len(self.df[self.df['nilai'] >= threshold])
        total_data = len(self.df)
        
        if total_data == 0:
            return 0.0
        
        persentase = (jumlah_lulus / total_data) * 100
        return round(persentase, 2)

    def save_summary(self, path: str):
        with open(path, 'a') as file:
            file.write("\n=== RINGKASAN GRADEBOOK (OOP) ===\n")
            file.write(f"Total Mahasiswa: {len(self.df)}\n")
            file.write(f"Rata-rata Kelas: {self.average()}\n")
            file.write(f"Persentase Kelulusan: {self.pass_rate()}%\n")

    def __str__(self):
        # output ringkas pas objek GradeBook di-print
        return f"GradeBook(Jumlah Data: {len(self.df)}, Rata-rata: {self.average()})"


if __name__ == "__main__":
    print("=== NUMPY ===")
    nilai_ujian = np.random.randint(50, 101, 10)
    
    rata_np = np.mean(nilai_ujian)
    median_np = np.median(nilai_ujian)
    std_np = np.std(nilai_ujian)
    min_np = np.min(nilai_ujian)
    max_np = np.max(nilai_ujian)

    print("Array Nilai Ujian:", nilai_ujian)
    print("Rata-rata:", round(rata_np, 2))
    print("Median:", median_np)
    print("Standar Deviasi:", round(std_np, 2))
    print("Nilai Min:", min_np)
    print("Nilai Max:", max_np)
    print()

    print("=== PANDAS ===")
    data_kelas = {
        "nama": ["Kharis", "Budi", "Andi", "Siti", "Joko"],
        "nim": ["21001", "21002", "21003", "21004", "21005"],
        "nilai": nilai_ujian[:5] 
    }
    df = pd.DataFrame(data_kelas)
    
    df['status'] = df['nilai'].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")
    
    print("5 Baris Pertama DataFrame:")
    print(df.head())
    print()

    nama_file = "ringkasan_tugas6.txt"
    jumlah_lulus = len(df[df['status'] == "LULUS"])
    jumlah_gagal = len(df[df['status'] == "TIDAK LULUS"])

    with open(nama_file, 'w') as f:
        f.write("=== STATISTIK NUMPY ===\n")
        f.write(f"Rata-rata: {round(rata_np, 2)}\n")
        f.write(f"Median: {median_np}\n")
        f.write(f"Standar Deviasi: {round(std_np, 2)}\n")
        f.write(f"Min: {min_np} | Max: {max_np}\n\n")
        
        f.write("=== RINGKASAN DATAFRAME ===\n")
        f.write(f"Jumlah Baris: {len(df)}\n")
        f.write(f"Jumlah Lulus: {jumlah_lulus}\n")
        f.write(f"Jumlah Tidak Lulus: {jumlah_gagal}\n")

    print("=== OOP: GRADEBOOK ===")
    buku_nilai = GradeBook(df)
    
    print(buku_nilai) 
    print("Rata-rata (OOP):", buku_nilai.average())
    print("Pass Rate (OOP):", buku_nilai.pass_rate(), "%")
    
    buku_nilai.save_summary(nama_file)
    print(f"\n[Info] Cek foldermu, file '{nama_file}' udah berhasil dibuat dan diisi!")