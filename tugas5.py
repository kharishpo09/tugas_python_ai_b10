def greet(nama: str) -> str:
    return f"Halo, {nama}!"

def tambah(a: float, b: float = 0.0) -> float:
    return a + b

def rata_rata(angka: list[float]) -> float:
    if not angka:
        return 0.0
    total = sum(angka)
    jumlah_data = len(angka)
    hasil = total / jumlah_data
    return round(hasil, 2)

class Student:
    def __init__(self, nama: str, nim: str):
        self.nama = nama
        self.nim = nim
        self.nilai: list[float] = [] 

    def tambah_nilai(self, skor: float):
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        if self.rata_nilai() >= threshold:
            return "LULUS"
        else:
            return "TIDAK LULUS"

    def __str__(self):
        rata = self.rata_nilai()
        stat = self.status()
        return f"Student(nama='{self.nama}', nim='{self.nim}', rata={rata}, status={stat})"

if __name__ == "__main__":
    
    print("=== FUNCTIONS ===")
    print(greet("Arifian"))
    print("Tambah (5, 7):", tambah(5, 7))
    print("Tambah (10 doang):", tambah(10))
    print("Rata-rata [80, 90, 100]:", rata_rata([80, 90, 100]))
    print("Rata-rata list kosong []:", rata_rata([]))
    print()

    print("=== CLASS STUDENT ===")
    mhs1 = Student(nama="Kharis", nim="21009876")
    mhs2 = Student(nama="Budi", nim="21001234")

    mhs1.tambah_nilai(85.5)
    mhs1.tambah_nilai(90.0)
    mhs1.tambah_nilai(78.5)

    mhs2.tambah_nilai(60.0)
    mhs2.tambah_nilai(65.5)
    mhs2.tambah_nilai(70.0)

    print(mhs1)
    print(mhs2)
    print()

    print(f"Rata-rata {mhs1.nama}: {mhs1.rata_nilai()} -> {mhs1.status()}")
    print(f"Rata-rata {mhs2.nama}: {mhs2.rata_nilai()} -> {mhs2.status()}")