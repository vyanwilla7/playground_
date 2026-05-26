# 📊 Prediksi Nilai Siswa — Supervised Learning

Proyek machine learning untuk memprediksi nilai mapel **saintek dan soshum** siswa berdasarkan nilai mapel wajib menggunakan algoritma **Linear Regression**.

-----

## 🎯 Tujuan

Memprediksi nilai 8 mata pelajaran (matematika TL, fisika, kimia, biologi, sosiologi, sejarah, ekonomi, geografi) berdasarkan nilai mata pelajaran wajib (matematika, bahasa Indonesia, bahasa Inggris, bahasa Sunda, PPKn, seni budaya, olahraga, informatika) dan umur siswa.

-----

## 📁 Struktur Project

```
prediksi_nilai_siswa/
├── data/
│   └── nilai_siswa.csv             # Dataset nilai 50 siswa
├── hasil_visualisasi/
│   ├── korelasi/                   # Heatmap korelasi per kelompok mapel
│   ├── distribusi_nilai/           # Histogram distribusi tiap mapel
│   └── perbandingan_antarsiswa/    # Lineplot perbandingan antar siswa
├── models/
│   └── model.pkl                   # Trained model (joblib)
├── main.py                         # Entry point & definisi class
├── requirements.txt
└── README.md
```

-----

## ⚙️ Tech Stack

|Library                 |Kegunaan                               |
|------------------------|---------------------------------------|
|`pandas`                |Load dan manipulasi dataset            |
|`numpy`                 |Operasi numerik                        |
|`scikit-learn`          |Preprocessing, training, evaluasi model|
|`matplotlib` & `seaborn`|Visualisasi data                       |
|`joblib`                |Menyimpan dan memuat model             |

-----

## 🔄 ML Pipeline

```
Load Data → EDA → Visualisasi → Preprocessing → Training → Evaluasi → Save/Load Model
```

1. **Load Data** — Membaca dataset CSV dan menampilkan preview
1. **EDA** — Mengecek missing value dan statistik deskriptif
1. **Visualisasi** — Heatmap korelasi, histogram distribusi, lineplot perbandingan siswa
1. **Preprocessing** — Feature selection, StandardScaler, train-test split (80:20)
1. **Training** — Melatih model Linear Regression
1. **Evaluasi** — Mengukur performa model dengan MSE dan R² Score
1. **Save/Load Model** — Menyimpan dan memuat model menggunakan joblib

-----

## 📈 Hasil Evaluasi Model

|Metrik      |Nilai |
|------------|------|
|**MSE**     |1.7800|
|**R² Score**|0.9849|

Model mencapai R² Score **0.9849** — artinya si model ini mampu menjelaskan **98.49%** variasi nilai mapel saintek dan soshum berdasarkan nilai mapel wajib.

-----

## 🚀 Cara Menjalankan

**1. Clone repository**

```bash
git clone https://github.com/vyanwilla7/prediksi-nilai-siswa.git
cd prediksi-nilai-siswa
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Jalankan program**

```bash
python main.py
```

-----

## 📦 Requirements

```
pandas
numpy
scikit-learn
matplotlib
seaborn
joblib
```

-----

## Text editor

```
Neovim

```
-----

## 👤 Author

**vyanwilla7** — [GitHub](https://github.com/vyanwilla7)
