"""Sistem Pakar Rekomendasi Karier (Forward Chaining)

Alur: pengguna menjawab pertanyaan minat (y/n) -> jawaban 'y' menjadi fakta ->
mesin inferensi mengulang aturan JIKA-MAKA sampai tidak ada fakta baru ->
tampil rekomendasi karier beserta aturan yang aktif.
"""

# Daftar minat/keahlian: kode_fakta -> pertanyaan
GEJALA = {
    "suka_logika": "Apakah kamu suka berpikir logis dan menyusun algoritma?",
    "suka_komputer": "Apakah kamu suka bekerja dengan komputer?",
    "suka_menggambar": "Apakah kamu suka menggambar atau mendesain tampilan?",
    "suka_angka": "Apakah kamu suka bekerja dengan angka dan data?",
    "suka_berbicara": "Apakah kamu suka berbicara dan presentasi di depan orang?",
    "suka_menulis": "Apakah kamu suka menulis atau membuat dokumentasi?",
    "suka_elektronik": "Apakah kamu suka merakit atau mengutak-atik elektronik?",
    "suka_memecahkan_masalah": "Apakah kamu suka memecahkan masalah yang rumit?",
    "suka_bekerja_tim": "Apakah kamu suka bekerja dalam tim?",
    "suka_riset": "Apakah kamu suka meneliti dan mencari tahu hal baru?",
}

# Aturan: (syarat, kesimpulan). Kesimpulan boleh menjadi fakta antara (bakat_...)
ATURAN = [
    # Tahap 1: minat -> bakat (fakta antara)
    ({"suka_logika", "suka_komputer"}, "bakat_pemrograman"),
    ({"suka_angka", "suka_riset"}, "bakat_analisis"),
    ({"suka_menggambar", "suka_komputer"}, "bakat_desain"),
    ({"suka_berbicara", "suka_bekerja_tim"}, "bakat_komunikasi"),
    ({"suka_elektronik", "suka_memecahkan_masalah"}, "bakat_teknik"),
    # Tahap 2: bakat -> karier (kesimpulan akhir)
    ({"bakat_pemrograman", "suka_memecahkan_masalah"}, "software_engineer"),
    ({"bakat_pemrograman", "bakat_analisis"}, "data_scientist"),
    ({"bakat_analisis", "suka_komputer"}, "data_analyst"),
    ({"bakat_desain", "suka_bekerja_tim"}, "ui_ux_designer"),
    ({"bakat_teknik", "suka_komputer"}, "automation_engineer"),
    ({"bakat_teknik", "suka_logika"}, "embedded_iot_engineer"),
    ({"bakat_komunikasi", "suka_logika"}, "it_project_manager"),
    ({"bakat_komunikasi", "suka_menulis"}, "technical_writer"),
]

# Kesimpulan akhir beserta penjelasannya
KARIER = {
    "software_engineer": "Software Engineer - membuat dan memelihara aplikasi.",
    "data_scientist": "Data Scientist - menganalisis data dan membangun model AI.",
    "data_analyst": "Data Analyst - mengolah data menjadi informasi bisnis.",
    "ui_ux_designer": "UI/UX Designer - merancang tampilan dan pengalaman pengguna.",
    "automation_engineer": "Automation Engineer - merancang sistem otomasi (PLC, HMI).",
    "embedded_iot_engineer": "Embedded/IoT Engineer - memprogram perangkat elektronik pintar.",
    "it_project_manager": "IT Project Manager - memimpin tim proyek teknologi.",
    "technical_writer": "Technical Writer - menyusun dokumentasi teknis.",
}


def tanya_gejala():
    """Mengajukan pertanyaan; jawaban 'y' menjadi fakta."""
    fakta = set()
    for kode, pertanyaan in GEJALA.items():
        jawab = input(f"{pertanyaan} (y/n): ").strip().lower()
        if jawab == "y":
            fakta.add(kode)
    return fakta


def inferensi(fakta):
    """Forward chaining: ulangi aturan sampai tidak ada fakta baru."""
    riwayat = []  # catatan aturan yang aktif (untuk penjelasan)
    ada_baru = True
    while ada_baru:
        ada_baru = False
        for syarat, hasil in ATURAN:
            if syarat <= fakta and hasil not in fakta:
                fakta.add(hasil)
                riwayat.append((syarat, hasil))
                ada_baru = True
    return riwayat


def main():
    print("=== Sistem Pakar Rekomendasi Karier ===")
    print("Jawab dengan y (ya) atau n (no).\n")
    fakta = tanya_gejala()
    riwayat = inferensi(fakta)

    rekomendasi = [k for k in KARIER if k in fakta]
    print("\n--- Rekomendasi Karier ---")
    if not rekomendasi:
        print("Belum ada rekomendasi. Coba jawab 'y' pada lebih banyak pertanyaan.")
    for r in rekomendasi:
        print("-", KARIER[r])

    print("\n--- Penjelasan (aturan yang aktif) ---")
    for syarat, hasil in riwayat:
        print(f"JIKA {' dan '.join(sorted(syarat))} MAKA {hasil}")


if __name__ == "__main__":
    main()
