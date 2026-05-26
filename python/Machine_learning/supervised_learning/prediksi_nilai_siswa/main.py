import os
from typing import Optional

import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

class PrediksiNilai:

    def __init__(self, data_path: str) -> None:
        self.data: str = data_path
        self.df: Optional[pd.DataFrame] = None
        self.X: Optional[pd.DataFrame] = None
        self.y: Optional[pd.DataFrame] = None
        self.X_train: Optional[np.ndarray] = None
        self.X_test: Optional[np.ndarray] = None
        self.y_train: Optional[pd.DataFrame] = None
        self.y_test: Optional[pd.DataFrame] = None
        self.scaler: Optional[StandardScaler] = None
        self.model: Optional[LinearRegression] = None

    def load_data(self) -> None:
        if not os.path.exists(self.data):
            raise FileNotFoundError(f"file tidak di temukan: {self.data}")

        self.df = pd.read_csv(self.data)
        print(self.df.head())

    def eda(self) -> None:
        if self.df is None:
            raise ValueError("data harus di load terlebih dahulu!")

        missing_value = self.df.isna().sum()

        if sum(missing_value) == 0:
            print("data anda bersih, tidak ada missing value!")
        else:
            print("ada data yang bernilai NaN!")

        describe_data = self.df.describe()
        korelasi = self.df.corr(numeric_only=True)

        print(f"describe data: {describe_data}\nkorelasi: {korelasi}")

    def visualisasi_data(self) -> None:
        # korelasi heatmap
        mapel_saintek = ["fisika", "kimia", "matematika_tl", "biologi"]
        mapel_soshum = ["sosiologi", "ekonomi", "geografi", "sejarah"]
        mapel_wajib = ["bahasa_inggris", "bahasa_indonesia", "bahasa_sunda", "ppkn", "matematika", "olahraga", "informatika", "seni_budaya"]

        sns.heatmap(self.df[mapel_saintek + ["umur"]].corr(), annot=True, fmt=".2f", cmap="coolwarm")# type:ignore
        plt.title("korelsi mapel saintek")
        plt.savefig("hasil_visualisasi/korelasi/korelasi_saintek.png")
        plt.clf()

        sns.heatmap(self.df[mapel_soshum + ["umur"]].corr(), annot=True, fmt=".2f", cmap="coolwarm")# type:ignore
        plt.title("korelsi mapel soshum")
        plt.savefig("hasil_visualisasi/korelasi/korelasi_soshum.png")
        plt.clf()

        sns.heatmap(self.df[mapel_wajib + ["umur"]].corr(), annot=True, fmt=".2f", cmap="coolwarm")# type:ignore
        plt.title("korelsi mapel wajib")
        plt.savefig("hasil_visualisasi/korelasi/korelasi_mapelwajib.png")
        plt.clf()

        # distribusi histogram
        kolom_nilai = self.df.select_dtypes(include='number').columns# type:ignore

        for kolom in kolom_nilai:
            plt.figure(figsize=(6, 4))
            sns.histplot(self.df[kolom])# type:ignore
            plt.title(f"histogram {kolom}")
            plt.xlabel("nilai")
            plt.ylabel("jumlah siswa")
            plt.savefig(f"hasil_visualisasi/distribusi_nilai/histogram_{kolom}.png")
            plt.clf()

        # perbandingan antar siswa lineplot
        self.df["rata-rata_saintek"] = self.df[mapel_saintek].mean(axis=1)# type:ignore
        self.df["rata-rata_soshum"] = self.df[mapel_soshum].mean(axis=1)# type:ignore
        self.df["rata-rata_wajib"] = self.df[mapel_wajib].mean(axis=1)# type:ignore

        plt.figure(figsize=(10, 8))
        sns.lineplot(data=self.df, x="nama", y="rata-rata_saintek", label="saintek", marker="o")
        sns.lineplot(data=self.df, x="nama", y="rata-rata_soshum", label="soshum", marker="o")
        sns.lineplot(data=self.df, x="nama", y="rata-rata_wajib", label="wajib", marker="o")
        plt.xticks(rotation=45)
        plt.title("perbandingan nilai mapel wajib, saintek, dan soshum")
        plt.xlabel("nama siswa")
        plt.ylabel("rata' nilai")
        plt.tight_layout()
        plt.savefig("hasil_visualisasi/perbandingan_antarsiswa/lineplot_kelompok.png")
        plt.clf()

    def preprocessing(self) -> None:
        if self.df is None:
            raise ValueError("data perlu di load terlebih dahulu!")

        df_drop = self.df.drop(columns=["nama"])

        self.X = df_drop[["umur", "matematika", "bahasa_inggris", "bahasa_indonesia", "bahasa_sunda", "olahraga", "informatika", "seni_budaya", "ppkn"]]# type:ignore
        self.y = df_drop[["matematika_tl", "fisika", "biologi", "kimia", "sosiologi","sejarah", "ekonomi", "geografi"]]# type:ignore

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(self.X)

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X_scaled, self.y, test_size=0.2, random_state=42)# type:ignore

        print("tahap preprocessing telah sukses!")
        print(f"X_train: {self.X_train}\nX_test: {self.X_test}")

    def training_model(self) -> None:
        if self.X_train is None:
            raise ValueError("perlu di lakukan tahap preprocessing terlebih dahulu!")

        self.model = LinearRegression()
        self.model.fit(self.X_train, self.y_train)# typr: ignore

        print("\ntraining model telah sukses di lakukan!")

    def evaluasi_model(self) -> None:
        # self.model.fit(self.X_train, self.y_train)# typr: ignore

        y_pred = self.model.predict(self.X_test)# typr: ignore
        mse = mean_squared_error(self.y_test, y_pred)
        r2s = r2_score(self.y_test, y_pred)

        print("tahap evaluasi model telah sukses!")
        print(f"hasil mse: {mse:.4f}\nhasil r2s: {r2s:.4f}")

    def save_model(self, path: str) -> None:
        if self.model is None:
            raise ValueError("perlu di lakukan tahap training dulu")

        os.makedirs(os.path.dirname(path), exist_ok=True)
        joblib.dump(self.model, path)
        print(f"save model telah sukses!\nmodel disimpan di: {path}")

    def load_model(self, path: str) -> None:
        if not os.path.exists(path):
            raise FileNotFoundError(f"file tidak di temukan: {path}")

        self.model = joblib.load(path)
        print(f"model berhasil di load dari {path}")

  
def main() -> None:
    pembatas: str = "="*50
    try:
        df = PrediksiNilai("data/nilai_siswa.csv")
        df.load_data()
        print(pembatas)

        df.eda()
        print(pembatas)

        df.visualisasi_data()
        print(pembatas)

        df.preprocessing()
        print(pembatas)
        
        df.training_model()
        print(pembatas)

        df.evaluasi_model()
        print(pembatas)

        df.save_model("models/model.pkl")
        print(pembatas)

        df.load_model("models/model.pkl")
        print(pembatas)

        df.evaluasi_model()
        print(pembatas)
    except Exception as e:
        print(f"proses gagal!, telah terjadi error: {e}")

if __name__ == "__main__":
    main()
