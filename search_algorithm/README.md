# 🧭 Pathfinding Visualization

Aplikasi visualisasi algoritma pencarian jalur (*pathfinding*) pada grid 2D, dibuat dengan **Python**, **Pygame**, dan **Tkinter**. Kamu bisa menggambar rintangan sendiri, menentukan titik awal dan akhir, lalu melihat langkah demi langkah bagaimana tiap algoritma menjelajahi grid untuk menemukan jalur.

---

## 📑 Daftar Isi

- [Fitur](#-fitur)
- [Algoritma yang Tersedia](#-algoritma-yang-tersedia)
- [Tampilan & Kode Warna](#-tampilan--kode-warna)
- [Persyaratan](#-persyaratan)
- [Instalasi](#-instalasi)
- [Cara Menjalankan](#-cara-menjalankan)
- [Cara Penggunaan](#-cara-penggunaan)
- [Hasil Running](#-hasil-running)
- [Kontrol Keyboard & Mouse](#-kontrol-keyboard--mouse)
- [Struktur Proyek](#-struktur-proyek)
- [Cara Kerja Singkat](#-cara-kerja-singkat)
- [Konfigurasi](#-konfigurasi)
- [Batasan & Catatan](#-batasan--catatan)
- [Pengembangan Selanjutnya](#-pengembangan-selanjutnya)
- [Kontribusi](#-kontribusi)
- [Lisensi](#-lisensi)

---

## ✨ Fitur

- **4 algoritma pathfinding**: A\*, Dijkstra, BFS, dan DFS.
- **Menu pemilihan algoritma** berbasis Tkinter, lengkap dengan pengaturan awal.
- **Gambar rintangan sendiri** dengan mouse (klik dan geser).
- **Generator maze acak** (±30% sel menjadi rintangan).
- **Atur kecepatan visualisasi** lewat slider maupun keyboard.
- **Mode *Smooth Transitions*** untuk animasi sel yang dikunjungi.
- **Pause / Resume** saat algoritma sedang berjalan.
- **Pengukur waktu eksekusi** yang dicetak di terminal.
- **Simpan screenshot** grid ke `maze.png` dengan satu tombol.
- Pindah algoritma dengan cepat memakai shortcut angka `1`–`4`.
- Notifikasi jika titik tujuan **tidak dapat dijangkau**.

---

## 🧠 Algoritma yang Tersedia

| Algoritma | Warna Sel Dikunjungi | Jalur Terpendek? | Strategi |
|-----------|----------------------|------------------|----------|
| **A\*** | 🔵 Biru | ✅ Ya | Priority queue dengan `cost + heuristic` (jarak Manhattan) |
| **Dijkstra** | 🟢 Hijau | ✅ Ya | Priority queue berdasarkan cost kumulatif |
| **BFS** | 🟣 Ungu | ✅ Ya (grid tanpa bobot) | Antrian FIFO, menjelajah per lapisan |
| **DFS** | 🟠 Oranye | ❌ Tidak | Stack LIFO, urutan tetangga diacak (`random.shuffle`) |

> **Catatan:** Pada grid ini setiap langkah berbiaya 1, sehingga Dijkstra dan BFS menghasilkan panjang jalur yang sama. Perbedaannya terletak pada struktur data yang dipakai. A\* biasanya mengunjungi lebih sedikit sel karena dipandu oleh heuristik.

---

## 🎨 Tampilan & Kode Warna

| Warna | Arti |
|-------|------|
| ⬛ Hitam | Sel kosong / belum dikunjungi |
| ⬜ Putih | Garis grid |
| 🔘 Abu-abu | Rintangan (obstacle) |
| 🟢 / 🔵 / 🟣 / 🟠 | Sel yang sudah dikunjungi (sesuai algoritma) |
| 🟡 Kuning | Jalur akhir yang ditemukan |
| 🖼️ Ikon `STARTEND.png` | Titik awal dan titik akhir |

---

## 📦 Persyaratan

- **Python 3.8+**
- Library:
  - [`pygame`](https://www.pygame.org/) – grafis dan input
  - [`Pillow`](https://python-pillow.org/) – membuka screenshot
  - [`numpy`](https://numpy.org/) – diimpor oleh program
- **Tkinter** (bawaan Python di Windows & macOS; di Linux mungkin perlu dipasang terpisah)
- File gambar **`STARTEND.png`** di folder yang sama dengan skrip (dipakai sebagai ikon titik awal/akhir).

---

## 🔧 Instalasi

1. **Clone repository**

```bash
   git clone https://github.com/<username>/<nama-repo>.git
   cd <nama-repo>
```

2. **(Opsional) Buat virtual environment**

```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
```

3. **Pasang dependensi**

```bash
   pip install pygame pillow numpy
```

4. **Khusus Linux** (jika Tkinter belum ada):

```bash
   sudo apt install python3-tk
```

5. Pastikan file `STARTEND.png` berada di folder yang sama dengan skrip utama.

---

## ▶️ Cara Menjalankan

```bash
python main.py
```

> Ganti `main.py` dengan nama file skrip kamu.

---

## 🕹️ Cara Penggunaan

1. **Jalankan program.** Jendela menu *Algorithm Selection* akan muncul.
2. Atur opsi di menu:
   - **Maze** – centang untuk membuat rintangan acak otomatis.
   - **Visualization Delay** – slider 0–200 ms (makin kecil makin cepat).
   - **Smooth Transitions** – animasi halus pada sel yang dikunjungi.
   - **Cell Size** – ukuran sel (20–50 px).
3. Klik salah satu tombol algoritma: **A\***, **Dijkstra's**, **BFS**, atau **DFS**.
4. Pada jendela grid:
   1. **Klik kiri pertama** → menentukan **titik awal**.
   2. **Klik kiri kedua** → menentukan **titik akhir**.
   3. **Klik kiri berikutnya** (boleh sambil digeser) → menggambar **rintangan**.
   4. **Klik kanan** pada rintangan → menghapusnya.
5. Tekan **`SPACE`** untuk menjalankan algoritma.
6. Setelah selesai, jalur akan digambar **kuning** dan waktu eksekusi tampil di terminal.
7. Tekan **`C`** untuk mengosongkan grid dan mencoba lagi.

---

## 📸 Hasil Running

Semua pengujian memakai skenario yang sama: sebuah **dinding vertikal (abu-abu)** di tengah grid dengan celah di bagian bawah, sehingga algoritma harus berputar mengelilingi dinding untuk mencapai **titik tujuan (ikon merah) di pojok kanan atas**.

### 1. A\* (A-Star)

![Hasil running A*](images/search_algorithm.png)

Sel yang dikunjungi berwarna **biru** dan jalur akhir berwarna **kuning**. A\* menyusuri sisi atas grid menuju tujuan dengan bantuan heuristik jarak Manhattan. Ketika terhalang dinding, A\* berputar mengelilingi ujung dinding lalu kembali naik ke titik tujuan. Jalur yang dihasilkan adalah **jalur terpendek**.

### 2. Dijkstra

![Hasil running Dijkstra](images/HASIL_RUNNING_DIJKSTRA.jpeg)

Sel yang dikunjungi berwarna **hijau**. Dijkstra menyebar ke **segala arah secara merata** (tanpa heuristik) sehingga hampir seluruh grid terjelajahi sebelum tujuan ditemukan. Jalur kuning mengitari ujung bawah dinding dan berakhir di titik tujuan. Jalur yang dihasilkan adalah **jalur terpendek**.

### 3. BFS (Breadth-First Search)

![Hasil running BFS](images/HASIL_RUNNING_BFS.jpeg)

Sel yang dikunjungi berwarna **ungu**. BFS menjelajah **lapis demi lapis** dari titik awal sehingga pola penyebarannya mirip Dijkstra. Jalur kuning juga melewati celah di bawah dinding. Panjang jalurnya **sama dengan Dijkstra** karena pada grid tanpa bobot keduanya sama-sama optimal; bentuk jalur bisa sedikit berbeda karena urutan tetangga yang diproses.

### 4. DFS (Depth-First Search)

![Hasil running DFS](images/HASIL_RUNNING_DFS.jpeg)

Sel yang dikunjungi berwarna **oranye**, sedangkan area **hitam** adalah sel yang tidak pernah dikunjungi. DFS menyelam sedalam mungkin sebelum mundur dan urutan tetangganya diacak, sehingga jalur kuning yang dihasilkan **sangat berkelok dan panjang**. Inilah alasan DFS **tidak menjamin jalur terpendek**, dan hasilnya bisa berbeda setiap kali dijalankan.

### Perbandingan Singkat

| Algoritma | Warna | Pola Penjelajahan | Jalur Akhir |
|-----------|-------|-------------------|-------------|
| A\* | 🔵 Biru | Terarah ke tujuan (heuristik) | Terpendek |
| Dijkstra | 🟢 Hijau | Menyebar merata ke segala arah | Terpendek |
| BFS | 🟣 Ungu | Menyebar lapis demi lapis | Terpendek |
| DFS | 🟠 Oranye | Menyelam dalam, acak | Panjang & berkelok (tidak optimal) |

---

## ⌨️ Kontrol Keyboard & Mouse

### Mouse

| Aksi | Fungsi |
|------|--------|
| Klik kiri (1×) | Set titik awal |
| Klik kiri (2×) | Set titik akhir |
| Klik kiri + geser | Gambar rintangan |
| Klik kanan | Hapus rintangan |

### Keyboard

| Tombol | Fungsi |
|--------|--------|
| `SPACE` | Jalankan algoritma terpilih |
| `P` | Pause / Resume (saat algoritma berjalan) |
| `ESC` | Saat algoritma berjalan: hentikan. Saat idle: buka menu pemilihan |
| `C` | Bersihkan grid & reset titik awal/akhir |
| `M` | Generate maze acak |
| `S` | Simpan screenshot ke `maze.png` dan tampilkan |
| `1` | Pilih A\* |
| `2` | Pilih Dijkstra |
| `3` | Pilih BFS |
| `4` | Pilih DFS |
| `+` / `=` | Tambah delay visualisasi (+10 ms) |
| `-` | Kurangi delay visualisasi (−10 ms) |
| `9` | Tambah delay sel dikunjungi (+10 ms) |
| `0` | Kurangi delay sel dikunjungi (−10 ms) |

---

## 🗂️ Struktur Proyek

```
.
├── main.py          # Skrip utama (logika algoritma, UI, dan event loop)
├── STARTEND.png     # Ikon penanda titik awal & akhir
├── images/          # Screenshot hasil running untuk dokumentasi
│   ├── search_algorithm.png          # Hasil A*
│   ├── HASIL_RUNNING_DIJKSTRA.jpeg   # Hasil Dijkstra
│   ├── HASIL_RUNNING_BFS.jpeg        # Hasil BFS
│   └── HASIL_RUNNING_DFS.jpeg        # Hasil DFS
├── maze.png         # (dibuat otomatis) hasil screenshot saat menekan "S"
└── README.md
```

### Fungsi-fungsi utama

| Fungsi | Deskripsi |
|--------|-----------|
| `create_menu()` | Membuat menu Tkinter (pilihan algoritma, slider delay & ukuran sel) |
| `run_algorithm()` | *Main loop* Pygame: menangani mouse, keyboard, dan menjalankan algoritma |
| `astar()` / `dijkstra()` / `bfs()` / `dfs()` | Implementasi masing-masing algoritma beserta visualisasinya |
| `heuristic()` | Heuristik jarak Manhattan untuk A\* |
| `neighbors()` | Mengembalikan tetangga valid (atas, bawah, kiri, kanan) |
| `generate_random_maze()` | Mengisi grid dengan rintangan acak |
| `draw_grid()` / `draw_cell()` | Menggambar grid dan sel berwarna |
| `visualize_path()` | Menganimasikan jalur akhir berwarna kuning |
| `remove_obstacle()` | Menghapus rintangan dan menggambar ulang garis grid |
| `reset()` | Mengosongkan layar dan menggambar ulang grid |

---

## ⚙️ Cara Kerja Singkat

Setiap algoritma menyimpan *frontier* (sel yang akan dikunjungi) beserta **jalur yang ditempuh** untuk mencapainya:

- **BFS** memakai `deque` sebagai antrian → sel dikunjungi berdasarkan jumlah langkah terkecil.
- **DFS** memakai `list` sebagai stack → menyelam sedalam mungkin sebelum mundur; urutan tetangga diacak sehingga jalur bisa berbeda tiap dijalankan.
- **Dijkstra** memakai `heapq` dengan prioritas `cost` (jumlah langkah dari titik awal).
- **A\*** memakai `heapq` dengan prioritas `cost + heuristic`, di mana heuristik adalah **jarak Manhattan** ke tujuan:

```
  h(n) = |x_n − x_goal| + |y_n − y_goal|
```

Ketika sel tujuan ditemukan, jalur yang tersimpan digambar dengan warna kuning. Bila frontier habis sebelum tujuan ditemukan, muncul pesan **"End node not reachable!"**.

### Kompleksitas (V = jumlah sel, E = jumlah sisi)

| Algoritma | Waktu | Optimal |
|-----------|-------|---------|
| BFS | O(V + E) | Ya (grid tanpa bobot) |
| DFS | O(V + E) | Tidak |
| Dijkstra | O((V + E) log V) | Ya |
| A\* | Bergantung heuristik, O((V + E) log V) kasus terburuk | Ya (heuristik admissible) |

---

## 🛠️ Konfigurasi

Beberapa konstanta di bagian atas kode dapat kamu ubah:

| Konstanta | Default | Keterangan |
|-----------|---------|------------|
| `GRID_SIZE` | `100` | Jumlah sel per sisi pada grid logis |
| `CELL_SIZE` | `20` | Ukuran satu sel dalam piksel |
| `SCREEN_SIZE` | `(800, 600)` | Ukuran jendela Pygame (alternatif: `1278, 660`) |
| `DELAY` | `50` | Jeda (ms) antar langkah visualisasi |
| `DELAY_VISITED` | `0` | Jeda (ms) tambahan saat menggambar sel dikunjungi |
| Probabilitas maze | `0.3` | Di `generate_random_maze()`, ubah `random.random() < 0.3` |

> 💡 **Tips benchmark:** untuk membandingkan kecepatan murni antar algoritma, set `DELAY` dan `DELAY_VISITED` ke `0` dan matikan *Smooth Transitions*.

---

## ⚠️ Batasan & Catatan

- Pada pengaturan default, **grid logis (100×100)** lebih besar daripada area yang tampil di jendela (800×600 dengan sel 20 px ≈ 40×30 sel). Sebaiknya tentukan titik awal dan akhir **di dalam area yang terlihat**, dan sesuaikan `GRID_SIZE` bila perlu.
- Waktu yang dicetak di terminal **sudah termasuk delay visualisasi**, sehingga bukan ukuran performa murni algoritma kecuali delay diatur ke 0.
- Pergerakan hanya **4 arah** (atas, bawah, kiri, kanan), tanpa diagonal.
- Program memerlukan file `STARTEND.png`; tanpa file tersebut, pemasangan titik awal/akhir akan menimbulkan error.
- Mengubah **Cell Size** lewat slider hanya menggambar ulang grid; untuk hasil terbaik, atur sebelum memilih algoritma.
- Tekan `ESC` saat algoritma berjalan untuk menghentikannya.
