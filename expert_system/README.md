# Sistem Pakar Rekomendasi Karier

## Introduction
Program ini adalah sistem pakar yang merekomendasikan karier berdasarkan minat dan kemampuan pengguna. Pengguna menjawab sepuluh pertanyaan dengan `y` (ya) atau `n` (tidak). Jawaban `y` menjadi fakta, lalu mesin inferensi menjalankan aturan JIKA-MAKA dengan metode forward chaining, yaitu mengulang aturan sampai tidak ada fakta baru yang bisa disimpulkan.

Penalaran berjalan dua tahap:
1. Minat menjadi bakat. Contoh: JIKA suka_angka dan suka_riset MAKA bakat_analisis.
2. Bakat menjadi karier. Contoh: JIKA bakat_analisis dan suka_komputer MAKA data_analyst.

Karier yang dapat direkomendasikan:
- Software Engineer
- Data Scientist
- Data Analyst
- UI/UX Designer
- Automation Engineer
- Embedded/IoT Engineer
- IT Project Manager
- Technical Writer

Setelah rekomendasi, program menampilkan penjelasan berupa aturan yang aktif, sehingga alur penalarannya dapat ditelusuri.

## Requirements
- Python 3.x
- Tidak ada library tambahan

## How to Use
1. Buka terminal di folder utama repository.
2. Jalankan program:
   `python expert_system/sistem_pakar_karier.py`
3. Jawab setiap pertanyaan dengan `y` atau `n`, lalu tekan Enter.
4. Setelah pertanyaan terakhir, program menampilkan rekomendasi karier dan aturan yang aktif. Jika belum ada rekomendasi, coba jawab `y` pada lebih banyak pertanyaan.

## Running
(Tempel screenshot hasil running di sini.)
