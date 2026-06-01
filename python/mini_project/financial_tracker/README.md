# 💰 Financial Tracker

> Aplikasi pencatat keuangan berbasis terminal untuk melacak pemasukan dan pengeluaran bulanan.

---

## 📋 Deskripsi

Financial Tracker adalah aplikasi CLI sederhana yang membantu kamu mencatat pemasukan dan pengeluaran harian. Data disimpan dalam format CSV dan dikelompokkan per bulan secara otomatis.

---

## ✨ Fitur

- ✅ Tambah & lihat data pengeluaran
- ✅ Tambah & lihat data pemasukan
- ✅ Auto-fill tanggal jika dilewati
- ✅ Validasi input otomatis
- ✅ Data tersimpan per bulan dalam format CSV
- ✅ Menampilkan total pengeluaran & pemasukan

---

## 🛠️ Teknologi

- **Python 3.10+**
- **CSV** — penyimpanan data lokal
- **dataclasses** — struktur data
- **datetime** — manajemen waktu

---

## Text Editor

- **Neovim**

---

## 🚀 Cara Pakai

### Prasyarat

Pastikan Python 3.10+ sudah terinstall:

```bash
python --version
```

### Instalasi

```bash
# Clone repository
git clone https://github.com/vyanwilla7/playground_.git

# Masuk ke direktori
cd playground_/python/mini_project/financial_tracker
```

### Menjalankan

```bash
python main.py
```

---

## 📖 Penggunaan

Setelah menjalankan program, pilih menu yang tersedia:

```
-------------------------------
1. =====TAMBAH PENGELUARAN=====
2. ======LIHAT PENGELUARAN=====
3. ======TAMBAH PEMASUKAN======
4. =======LIHAT PEMASUKAN======
5. ========EXIT PROGRAM========
-------------------------------
```

| Menu | Fungsi |
|------|--------|
| 1 | Tambah data pengeluaran |
| 2 | Lihat semua pengeluaran bulan ini |
| 3 | Tambah data pemasukan |
| 4 | Lihat semua pemasukan bulan ini |
| 5 | Keluar program |

> 💡 **Tip:** Input tanggal bisa dikosongkan, otomatis terisi tanggal hari ini.

---

## 📁 Struktur Proyek

```
financial_tracker/
├── main.py               # File utama
├── data_pengeluaran/     # Folder data pengeluaran (auto-generated)
│   └── pengeluaran_bulan(N).csv
├── data_pemasukan/       # Folder data pemasukan (auto-generated)
│   └── pemasukan_bulan(N).csv
├── .gitignore
└── README.md
```

---

## 👨‍💻 Author

**vyanwilla7** — [github.com/vyanwilla7](https://github.com/vyanwilla7)
