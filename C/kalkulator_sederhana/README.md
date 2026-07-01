# Kalkulator Sederhana (C)

Kalkulator sederhana berbasis bahasa C dengan CLI (Command Line Interface).  
Project ini dibuat untuk latihan dasar pemrograman C seperti fungsi, loop, percabangan, dan modular programming.

---

## Fitur

- Operasi dasar:
  - Penjumlahan
  - Pengurangan
  - Perkalian
  - Pembagian
- Menu berbasis terminal
- Program berjalan dalam loop sampai user memilih keluar
- Handling pembagian dengan nol
- Struktur modular (header + source file)
- Build system sederhana menggunakan Makefile

---

## 📁 Struktur Project

```

/C/kalkulator_sederhana
│── src/
│   ├── main.c
│   ├── kalkulator.c
│── include/
│   ├── kalkulator.h
│── build/
│── Makefile
│── README.md

````

---

## Cara Compile

Gunakan `make`:

```bash
make
````

---

## Cara Menjalankan

```bash
make run
```

---

## Membersihkan Build

```bash
make clear
```

---

## Contoh Penggunaan

```
===== KALKULATOR SEDERHANA =====

pilih operator:
1. Penjumlahan
2. Pengurangan
3. Perkalian
4. Pembagian
0. Exit

> 1
masukkan angka pertama: 10
masukkan angka kedua: 5

hasil penjumlahan: 15.00
```

---

## Konsep yang Dipelajari

* Bahasa C dasar
* Function & modular programming
* Loop (`while`)
* Conditional (`if`, `switch-case`)
* Input/output (`scanf`, `printf`)
* Struktur project C sederhana
* Build automation dengan Makefile

---

## Tujuan Project

Project ini dibuat untuk:

* Latihan logika dasar pemrograman C
* Membuat program CLI sederhana
* Memahami struktur project yang rapi
* Belajar build system sederhana (Makefile)

## Author

**vyanwilla7** — [github.com/vyanwilla7](https://github.com/vyanwilla7)
