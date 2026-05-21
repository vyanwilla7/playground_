# QR Generator 

Mini Project QR Generator sederhana menggunakan bahasa pemrograman python.

## Features1
- Generate QR dari URL/Text
- Custom warna QR
- Custom background
- Save ke PNG
- Optional logo di tengah QR

---

## Struktur Project

```text
qr-generator/
│
├── main.py
├── qr_gen.py
│
├── logo/
├── outputs/
│
└── README.md
```

---

## Install

```bash
pip install 'qrcode[pil]'
```

---

## Run

```bash
python main.py
```

atau

```bash
python3 main.py
```

---

## Example

```text
Masukkan URL/Text : https://github.com/vyanwilla7/project_/blob/main/python/mini_project #wajib

Pilih warna QR [default= white] : green #optional

Pilih warna background QR [default= black] : black #optional

Buat nama file, [default name= qrcode] : mylinkedin #optional

Apakah anda akan menambahkan logo dalam QR anda? (y/n) : y #optional (jika anda ketik y, maka anda di haruskan untuk memasukkan file path, sebagai contoh: Masukka path: logo/foto_anda.png)

Apakah anda ingin mambuat QR Code lagi? (y/n) #jika ingin membuat lagi maka ketik 'y' dan jika ingin keluar dari program maka ketik 'n'
```

---

## Tech
- Python
- qrcode
- Pillow

---

