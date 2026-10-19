from collections import deque
from expert_system.sistem_pakar_karier import tanya_gejala, inferensi, KARIER

# Graf roadmap: dari kondisi awal menuju karier (node karier memakai kode dari KARIER)
GRAF = {
    "Mahasiswa": ["Dasar Pemrograman", "Statistika", "Desain Dasar",
                  "Komunikasi Teknis", "Elektronika Dasar"],
    "Dasar Pemrograman": ["Struktur Data", "Pemrograman Mikrokontroler"],
    "Struktur Data": ["software_engineer", "Machine Learning"],
    "Statistika": ["SQL dan Visualisasi", "Machine Learning"],
    "SQL dan Visualisasi": ["data_analyst"],
    "Machine Learning": ["data_scientist"],
    "Desain Dasar": ["Prototyping"],
    "Prototyping": ["ui_ux_designer"],
    "Komunikasi Teknis": ["Manajemen Proyek", "Dokumentasi Teknis"],
    "Manajemen Proyek": ["it_project_manager"],
    "Dokumentasi Teknis": ["technical_writer"],
    "Elektronika Dasar": ["PLC dan HMI", "Pemrograman Mikrokontroler"],
    "PLC dan HMI": ["automation_engineer"],
    "Pemrograman Mikrokontroler": ["embedded_iot_engineer"],
}


def nama_tampil(node):
    return KARIER[node].split(" - ")[0] if node in KARIER else node


class Bus:
    """Jalur pesan antar agen."""
    def __init__(self):
        self.agen = {}
        self.antrian = deque()

    def daftar(self, agen):
        self.agen[agen.nama] = agen

    def kirim(self, dari, ke, isi):
        self.antrian.append((dari, ke, isi))

    def jalankan(self):
        while self.antrian:
            dari, ke, isi = self.antrian.popleft()
            print(f"[pesan] {dari} -> {ke}: {isi['tipe']}")
            self.agen[ke].terima(dari, isi)


class Agen:
    def __init__(self, nama, bus):
        self.nama = nama
        self.bus = bus
        bus.daftar(self)

    def kirim(self, tujuan, isi):
        self.bus.kirim(self.nama, tujuan, isi)

    def terima(self, pengirim, isi):
        pass


class Konselor(Agen):
    """Agen sistem pakar."""
    def terima(self, pengirim, isi):
        if isi["tipe"] == "mulai":
            fakta = tanya_gejala()
            riwayat = inferensi(fakta)
            rekomendasi = [k for k in KARIER if k in fakta]
            self.kirim("Koordinator", {
                "tipe": "hasil_konsultasi",
                "rekomendasi": rekomendasi,
                "riwayat": riwayat,
            })


class Perencana(Agen):
    """Agen pencari jalur (BFS)."""
    def terima(self, pengirim, isi):
        if isi["tipe"] == "minta_jalur":
            jalur = self.bfs("Mahasiswa", isi["tujuan"])
            self.kirim("Koordinator", {
                "tipe": "jalur",
                "tujuan": isi["tujuan"],
                "jalur": jalur,
            })

    def bfs(self, awal, tujuan):
        antrian = deque([[awal]])
        dikunjungi = {awal}
        while antrian:
            jalur = antrian.popleft()
            if jalur[-1] == tujuan:
                return jalur
            for tetangga in GRAF.get(jalur[-1], []):
                if tetangga not in dikunjungi:
                    dikunjungi.add(tetangga)
                    antrian.append(jalur + [tetangga])
        return None


class Koordinator(Agen):
    """Agen pengatur alur dan penampil hasil."""
    def terima(self, pengirim, isi):
        if isi["tipe"] == "hasil_konsultasi":
            rekomendasi = isi["rekomendasi"]
            if not rekomendasi:
                print("\nBelum ada rekomendasi. Coba jawab 'y' pada lebih banyak pertanyaan.")
                return
            print("\n--- Rekomendasi Karier ---")
            for r in rekomendasi:
                print("-", KARIER[r])
            print("\n--- Penjelasan (aturan yang aktif) ---")
            for syarat, hasil in isi["riwayat"]:
                print(f"JIKA {' dan '.join(sorted(syarat))} MAKA {hasil}")
            print()
            for r in rekomendasi:
                self.kirim("Perencana", {"tipe": "minta_jalur", "tujuan": r})
        elif isi["tipe"] == "jalur":
            tujuan = nama_tampil(isi["tujuan"])
            if isi["jalur"]:
                langkah = " -> ".join(nama_tampil(n) for n in isi["jalur"])
                print(f"\nJalur menuju {tujuan}:\n  {langkah}")
            else:
                print(f"\nJalur menuju {tujuan} tidak ditemukan.")


def main():
    print("=== Multi Agent System: Konselor Karier ===")
    print("Jawab dengan y (ya) atau n (no).\n")
    bus = Bus()
    koordinator = Koordinator("Koordinator", bus)
    Konselor("Konselor", bus)
    Perencana("Perencana", bus)
    koordinator.kirim("Konselor", {"tipe": "mulai"})
    bus.jalankan()

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
