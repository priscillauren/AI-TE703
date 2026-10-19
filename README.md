# Pathfinding Visualizer

## Introduction
Program ini memvisualisasikan cara kerja algoritma pencarian jalur pada sebuah grid. Pengguna dapat memilih salah satu dari empat algoritma, yaitu A*, Dijkstra, BFS, dan DFS, lalu melihat proses pencarian dari titik awal menuju titik tujuan secara langkah demi langkah, sehingga perbedaan cara kerja tiap algoritma dapat dibandingkan.

## Requirements
- Python 3.x
- pygame
- numpy
- Pillow

Instal library dengan:
`pip install pygame numpy pillow`

## How to Use
1. Buka terminal di folder `search_algorithm`.
2. Jalankan program (harus dari dalam folder ini agar file `STARTEND.png` terbaca):
   `python Pathfinder.Comparison.py`
3. Di panel pengaturan, atur Maze, Visualization Delay, Smooth Transitions, dan Cell Size, lalu klik salah satu algoritma: A*, Dijkstra's, BFS, atau DFS.
4. Di jendela grid:
   - Klik kiri satu kotak untuk titik awal, lalu klik kiri kotak lain untuk titik tujuan.
   - Klik kiri lagi (boleh sambil digeser) untuk menggambar dinding. Klik kanan untuk menghapus dinding.
   - Tekan Spasi untuk menjalankan algoritma.
5. Tombol lain: P (jeda), C (hapus grid), M (maze acak), 1-4 (ganti algoritma), Esc (kembali ke menu).

## Running
(Tempel screenshot hasil running di sini.)
