<div align="center">

# Pathfinding Visualizer

**A\* · Dijkstra · BFS · DFS**

Bagian **Dev 1** dari proyek [AI-TE703](https://github.com/priscillauren/AI-TE703)

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Library](https://img.shields.io/badge/GUI-pygame-green)
![Algoritma](https://img.shields.io/badge/Algoritma-A*%20%7C%20Dijkstra%20%7C%20BFS%20%7C%20DFS-orange)

</div>

---

## Daftar Isi

1. [Introduction](#introduction)
2. [Algoritma yang Dibandingkan](#algoritma-yang-dibandingkan)
3. [Requirements](#requirements)
4. [Struktur Folder](#struktur-folder)
5. [How to Use](#how-to-use)
6. [Running](#running)
7. [Sources](#sources)
8. [Kontributor](#kontributor)

---

## Introduction

Program ini adalah visualisasi interaktif algoritma pencarian jalur (*pathfinding*) pada grid 2D. Program mensimulasikan dan membandingkan bagaimana berbagai algoritma menavigasi rute dari **titik awal (start)** ke **titik tujuan (end)** sambil melewati rintangan atau dinding.

Dengan visualisasi, perbedaan antar algoritma bisa dilihat langsung: sel mana saja yang dijelajahi dan seberapa panjang jalur akhirnya. Hal ini lebih mudah dipahami daripada hanya membaca teori.

**Tujuan program:** membandingkan cara kerja dan hasil empat algoritma pencarian jalur pada masalah yang sama.

---

## Algoritma yang Dibandingkan

| Algoritma | Cara kerja singkat | Menjamin jalur terpendek? |
|---|---|:-:|
| **A\*** | Menjelajah dengan bantuan heuristik (perkiraan jarak ke tujuan), sehingga biasanya menjelajah lebih sedikit sel. | Ya, jika heuristiknya admissible |
| **Dijkstra** | Selalu memperluas sel dengan biaya terkecil lebih dulu, menjelajah ke segala arah. | Ya |
| **BFS** | Menjelajah lapis demi lapis dari titik awal. | Ya, pada grid tanpa bobot |
| **DFS** | Menyelam sedalam mungkin pada satu arah sebelum mundur. | Tidak |

**Ringkasannya:**
- A\* dan Dijkstra sama-sama optimal, tetapi A\* biasanya lebih hemat penjelajahan.
- BFS cocok untuk grid tanpa bobot, tetapi menjelajah banyak sel.
- DFS bisa cepat menemukan jalur, tetapi jalurnya sering panjang dan berkelok.

---

## Requirements

| Kebutuhan | Keterangan |
|---|---|
| Python | Versi 3.x |
| pygame | Menampilkan jendela GUI dan animasi |
| numpy | Pengelolaan data grid |
| Pillow | Pengolahan gambar |

Install semua library sekaligus:

```
pip install pygame numpy pillow
```

---

## Struktur Folder

```
AI-TE703/
├── search_algorithm/
│   ├── Pathfinder.Comparison.py    # program utama
│   └── README.md                   # dokumen ini
├── expert_system/                  # bagian Dev 2
├── screenshots/                    # gambar hasil running
└── README.md                       # README utama proyek
```

---

## How to Use

**1. Clone repository**

```
git clone https://github.com/priscillauren/AI-TE703.git
```

**2. Masuk ke folder program**

Program harus dijalankan dari **dalam** folder `search_algorithm`.

```
cd AI-TE703/search_algorithm
```

**3. Install library**

```
pip install pygame numpy pillow
```

**4. Jalankan program**

```
python Pathfinder.Comparison.py
```

**5. Ikuti instruksi di layar**

Pilih algoritma lewat jendela GUI, lalu amati bagaimana algoritma tersebut mencari jalur dari start ke end.

> **Catatan:** kalau muncul error file atau gambar tidak ditemukan, hampir selalu penyebabnya program dijalankan dari folder yang salah. Pastikan terminal berada di dalam `search_algorithm`.

---

## Running

Contoh tampilan program saat dijalankan:

| A\* | Dijkstra |
|:-:|:-:|
| <img width="420" alt="A*" src="https://github.com/user-attachments/assets/ce523cad-7307-4baf-96dd-c7154e0f35e6" /> | <img width="420" alt="Dijkstra" src="https://github.com/user-attachments/assets/98ccdb47-cb18-41f4-9815-1049e5e8d61e" /> |

| BFS | DFS |
|:-:|:-:|
| <img width="420" alt="BFS" src="https://github.com/user-attachments/assets/9d361871-0f42-4bf5-a282-3ca896e69ade" /> | <img width="420" alt="DFS" src="https://github.com/user-attachments/assets/34fcbbe9-a498-4c65-a19e-a15cd0aee50a" /> |

---

## Sources

| Repository | Deskripsi |
|---|---|
| [Jitanshu-commits/Pathfinding](https://github.com/Jitanshu-commits/Pathfinding) | Visualisasi interaktif algoritma pencarian jalur pada kisi 2D (grid) yang mensimulasikan dan membandingkan bagaimana berbagai algoritma menavigasi rute dari titik awal ke tujuan di antara rintangan. |

---

## Kontributor

| Peran | Nama | GitHub |
|---|---|---|
| Dev 1 | irva | @irvashellaurbach-png |

---

<div align="center">

Bagian dari proyek **AI-TE703**

</div>
