<div align="center">

# AI-TE703

**Sistem Pakar Rekomendasi Karier · Pathfinding Visualizer**

Dua program kecerdasan buatan: satu berbasis pengetahuan, satu berbasis pencarian.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Expert System](https://img.shields.io/badge/Sistem%20Pakar-Forward%20Chaining-2ea44f)
![Search](https://img.shields.io/badge/Pencarian-A*%20%7C%20Dijkstra%20%7C%20BFS%20%7C%20DFS-orange)

</div>

---

## Daftar Isi

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Struktur Folder](#struktur-folder)
4. [How to Use](#how-to-use)
5. [Running](#running)
6. [Pembagian Tugas](#pembagian-tugas)
7. [Sources](#sources)

---

## Introduction

Proyek ini terdiri dari dua program:

| No | Program | Deskripsi | Folder |
|:-:|---|---|---|
| 1 | **Sistem Pakar Rekomendasi Karier** | Merekomendasikan karier berdasarkan jawaban pengguna menggunakan aturan if-then (forward chaining). | [`expert_system/`](expert_system) |
| 2 | **Pathfinding Visualizer** | Visualisasi algoritma pencarian jalur pada grid dengan empat algoritma: A\*, Dijkstra, BFS, dan DFS, sehingga cara kerja dan hasil tiap algoritma bisa dibandingkan. | [`search_algorithm/`](search_algorithm) |

### Sistem Pakar Rekomendasi Karier

Pengguna menjawab sepuluh pertanyaan dengan `y` atau `n`. Jawaban `y` menjadi fakta, lalu mesin inferensi menjalankan aturan JIKA-MAKA dengan metode forward chaining sampai tidak ada fakta baru yang bisa disimpulkan. Hasilnya berupa rekomendasi karier.

### Pathfinding Visualizer

Pengguna menentukan titik awal (start), titik tujuan (end), dan dinding pada grid 2D, lalu program menampilkan bagaimana tiap algoritma mencari rute.

| Algoritma | Karakter singkat |
|---|---|
| **A\*** | Memakai heuristik (perkiraan jarak ke tujuan), biasanya menjelajah lebih sedikit sel. |
| **Dijkstra** | Menjamin jalur dengan biaya terkecil, menjelajah ke segala arah. |
| **BFS** | Menjelajah lapis demi lapis, menjamin langkah paling sedikit pada grid tanpa bobot. |
| **DFS** | Menyelam sedalam mungkin lebih dulu, cepat tetapi jalur tidak dijamin terpendek. |

---

## Requirements

| Program | Kebutuhan |
|---|---|
| Sistem Pakar | Python 3.x (tanpa library tambahan) |
| Pathfinding Visualizer | Python 3.x, `pygame`, `numpy`, `Pillow` |

Install library untuk Pathfinding Visualizer:

```
pip install pygame numpy pillow
```

---

## Struktur Folder

```
AI-TE703/
├── expert_system/
│   ├── sistem_pakar_karier.py     # program sistem pakar
│   └── README.md
├── search_algorithm/
│   ├── Pathfinder.Comparison.py   # program pathfinding visualizer
│   └── README.md
├── screenshots/                   # gambar hasil running
└── README.md                      # dokumen ini
```

---

## How to Use

1. Clone repository:
   ```
   git clone https://github.com/priscillauren/AI-TE703.git
   ```
2. Masuk ke folder proyek:
   ```
   cd AI-TE703
   ```
3. Install library (lihat [Requirements](#requirements)).
4. Jalankan sistem pakar:
   ```
   python expert_system/sistem_pakar_karier.py
   ```
5. Jalankan pathfinding visualizer (harus dari dalam folder `search_algorithm`):
   ```
   cd search_algorithm
   python Pathfinder.Comparison.py
   ```
6. Ikuti instruksi yang muncul di layar: jawab `y`/`n` untuk sistem pakar, dan pilih algoritma lewat jendela GUI untuk visualizer.

---

## Running

Tangkapan layar program saat dijalankan:

<p align="center">
  <img width="600" alt="Tampilan program" src="https://github.com/user-attachments/assets/12aa2d91-1034-4f2a-8a8c-d873576ac3d1" />
</p>

| A\* | Dijkstra |
|:-:|:-:|
| <img width="400" alt="A*" src="https://github.com/user-attachments/assets/ce523cad-7307-4baf-96dd-c7154e0f35e6" /> | <img width="400" alt="Dijkstra" src="https://github.com/user-attachments/assets/98ccdb47-cb18-41f4-9815-1049e5e8d61e" /> |

| BFS | DFS |
|:-:|:-:|
| <img width="400" alt="BFS" src="https://github.com/user-attachments/assets/9d361871-0f42-4bf5-a282-3ca896e69ade" /> | <img width="400" alt="DFS" src="https://github.com/user-attachments/assets/34fcbbe9-a498-4c65-a19e-a15cd0aee50a" /> |

---

## Pembagian Tugas

| Peran | Anggota | Branch | Bagian |
|---|---|---|---|
| Manager | [@priscillauren](https://github.com/priscillauren) | `main` | README utama, screenshot, merge pull request |
| Dev 1 | [@irvashellaurbach-png](https://github.com/irvashellaurbach-png) | `dev1` | Folder `search_algorithm/` |
| Dev 2 | [@zasq-zehan](https://github.com/zasq-zehan) | `dev2` | Folder `expert_system/` |

Setiap anggota mengerjakan bagiannya di branch masing-masing, lalu digabung ke `main` lewat pull request.

---

## Sources

**Sistem Pakar Rekomendasi Karier**

- [ashcode028/Career-prediction](https://github.com/ashcode028/Career-prediction): program Python dengan modul durable-rules dan aturan forward chaining untuk sistem penasihat karier.
- [Sarthak-10/Career-Advisory-System-with-forward-chaining-rules](https://github.com/Sarthak-10/Career-Advisory-System-with-forward-chaining-rules): proyek yang memakai modul durable-rules untuk membuat sistem penasihat karier dengan aturan forward chaining.

**Pathfinding Visualizer**

- [Jitanshu-commits/Pathfinding](https://github.com/Jitanshu-commits/Pathfinding): visualisasi interaktif algoritma pencarian jalur pada grid 2D yang mensimulasikan dan membandingkan bagaimana berbagai algoritma menavigasi rute dari titik awal ke tujuan di antara rintangan.
