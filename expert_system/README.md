<div align="center">

# 🧠 Sistem Pakar Rekomendasi Karier

**Forward chaining · Aturan JIKA-MAKA · Python**

Bagian **Dev 2** dari proyek [AI-TE703](https://github.com/priscillauren/AI-TE703)

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Metode](https://img.shields.io/badge/Metode-Forward%20Chaining-2ea44f)
![Branch](https://img.shields.io/badge/Branch-dev2-blue)

</div>

---

## 📑 Daftar Isi

1. [Introduction](#-introduction)
2. [Cara Kerja](#-cara-kerja)
3. [Istilah Penting](#-istilah-penting)
4. [Requirements](#-requirements)
5. [Struktur Folder](#-struktur-folder)
6. [How to Use](#-how-to-use)
7. [Running](#-running)
8. [Sources](#-sources)
9. [Kontributor](#-kontributor)

---

## 📌 Introduction

Program ini adalah **sistem pakar** yang merekomendasikan karier berdasarkan minat dan kemampuan pengguna.

Pengguna menjawab **sepuluh pertanyaan** dengan `y` (ya) atau `n` (tidak). Jawaban `y` diubah menjadi **fakta**, lalu **mesin inferensi** menjalankan aturan **JIKA-MAKA** dengan metode **forward chaining**, yaitu mengulang pemeriksaan aturan sampai tidak ada fakta baru yang bisa disimpulkan. Hasil akhirnya adalah rekomendasi karier yang paling sesuai dengan jawaban pengguna.

**Mengapa sistem pakar?** Pengetahuan tentang "minat dan kemampuan apa yang cocok dengan karier apa" bisa ditulis sebagai aturan. Hasilnya juga mudah dijelaskan, karena kita bisa menunjuk aturan mana yang menghasilkan sebuah rekomendasi.

**Mengapa forward chaining?** Di awal kita belum tahu kariernya. Yang kita punya hanya fakta dari jawaban pengguna, lalu kesimpulan diturunkan dari fakta itu. Alur ini sesuai dengan forward chaining, yang bergerak dari data menuju kesimpulan.

---

## ⚙️ Cara Kerja

```
┌──────────────┐    ┌────────────────┐    ┌───────────────────┐    ┌──────────────┐
│  10 pertanyaan│ -> │  Fakta awal    │ -> │  Mesin inferensi  │ -> │  Rekomendasi │
│  (y / n)      │    │  (jawaban "y") │    │  (forward chaining)│    │  karier      │
└──────────────┘    └────────────────┘    └───────────────────┘    └──────────────┘
                                                    ^   │
                                                    └───┘
                                       ulangi sampai tidak ada fakta baru
```

| Langkah | Proses |
|:-:|---|
| 1 | Program menampilkan pertanyaan satu per satu. |
| 2 | Pengguna menjawab `y` atau `n`. |
| 3 | Setiap jawaban `y` disimpan sebagai fakta. |
| 4 | Mesin inferensi memeriksa semua aturan JIKA-MAKA terhadap fakta yang ada. |
| 5 | Aturan yang syaratnya terpenuhi **menyimpulkan fakta baru**. |
| 6 | Langkah 4 sampai 5 diulang sampai tidak ada fakta baru. |
| 7 | Kesimpulan akhir ditampilkan sebagai rekomendasi karier. |

**Bentuk aturan:**

```
JIKA  <fakta 1> DAN <fakta 2> ...
MAKA  <fakta baru / kesimpulan>
```

---

## 📖 Istilah Penting

| Istilah | Arti |
|---|---|
| **Fakta** | Informasi yang dianggap benar, dalam program ini berasal dari jawaban `y`. |
| **Aturan (rule)** | Pernyataan JIKA-MAKA yang menghubungkan fakta dengan kesimpulan. |
| **Basis pengetahuan** | Kumpulan seluruh aturan. |
| **Mesin inferensi** | Bagian program yang menjalankan aturan terhadap fakta. |
| **Forward chaining** | Penalaran maju: dari fakta yang ada menuju kesimpulan. |

---

## 🧰 Requirements

| Kebutuhan | Keterangan |
|---|---|
| Python | Versi 3.x |
| Library tambahan | Tidak ada |

Cek versi Python dengan:

```bash
python --version
```

---

## 🗂️ Struktur Folder

```
AI-TE703/
├── expert_system/
│   ├── sistem_pakar_karier.py    # program utama sistem pakar
│   └── README.md                 # dokumen ini
├── search_algorithm/             # bagian Dev 1
├── screenshots/                  # gambar hasil running
└── README.md                     # README utama proyek
```

---

## 🚀 How to Use

**1. Clone repository**

```bash
git clone https://github.com/priscillauren/AI-TE703.git
```

**2. Masuk ke folder proyek**

```bash
cd AI-TE703
```

**3. Jalankan sistem pakar**

```bash
python expert_system/sistem_pakar_karier.py
```

**4. Jawab pertanyaan**

Ketik `y` jika **ya** atau `n` jika **tidak**, lalu tekan Enter. Setelah semua pertanyaan dijawab, program menampilkan rekomendasi karier.

> 💡 **Tips:** jalankan dari folder utama proyek (`AI-TE703`), bukan dari dalam folder `expert_system`, agar path pada perintah di atas sesuai.

---

## 🖼️ Running

Contoh tampilan program saat dijalankan:

![Hasil running sistem pakar](../screenshots/expert_system.png)

---

## 📚 Sources

Referensi yang dipakai sebagai acuan dalam membuat sistem pakar ini:

| No | Repository | Deskripsi |
|:-:|---|---|
| 1 | [ashcode028/Career-prediction](https://github.com/ashcode028/Career-prediction) | Program Python dengan modul durable-rules dan aturan forward chaining untuk sistem penasihat karier. |
| 2 | [Sarthak-10/Career-Advisory-System-with-forward-chaining-rules](https://github.com/Sarthak-10/Career-Advisory-System-with-forward-chaining-rules) | Proyek yang memakai modul durable-rules untuk membuat sistem penasihat karier dengan aturan forward chaining. |

---

## 👤 Kontributor

| Peran | Nama | GitHub | Branch |
|---|---|---|---|
| Dev 2 | zasq | [@zasq-zehan](https://github.com/zasq-zehan) | `dev2` |

---

<div align="center">

Bagian dari proyek **AI-TE703** · Sistem Pakar Rekomendasi Karier

</div>
