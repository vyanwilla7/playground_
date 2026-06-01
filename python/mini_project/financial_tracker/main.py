import os
import csv
from dataclasses import dataclass 
from typing import Optional
from datetime import datetime

@dataclass 
class Struct:
    nama_folder: str
    nama_file: str
    waktu: str
    kategori: str
    jumlah: str
    jenis: str

class FinancialTracker:
    def find_file(self, data: Struct) -> None:
        if not os.path.exists(data.nama_folder):
            os.makedirs(data.nama_folder)

        if not os.path.exists(f"{data.nama_folder}/{data.nama_file}"):
            with open(f"{data.nama_folder}/{data.nama_file}", 'w', newline='') as file:
                writter = csv.writer(file)
                writter.writerow([
                    "Waktu",
                    "Kategori",
                    "Jumlah",
                    "Jenis"
                    ])

    def tambah_data(self, data: Struct) -> Optional[int | str]:
        try:
            self.find_file(data)

            with open(f"{data.nama_folder}/{data.nama_file}", 'a', newline='') as file:
                writter = csv.writer(file)
                print("data berhasil di tambahkan!")

                return writter.writerow([data.waktu, data.kategori, data.jumlah, data.jenis])

        except Exception as e:
            print(f"gagal menyimpan data, terjadi error: {e}")

    def lihat_data(self, data: Struct) -> Optional[str]:
        try:
            if not os.path.exists(data.nama_folder):
                raise FileNotFoundError("folder tidak di temukan!")

            files = os.listdir(data.nama_folder)
            if len(files) == 1:
                file_pilihan = files[0]
            else:
                for i, file in enumerate(files, 1):
                    print(f"{i}.{file}")
                file_pilihan = int(input("pilih file: "))- 1
                file_pilihan = files[file_pilihan]

            with open(f"{data.nama_folder}/{file_pilihan}", 'r') as file:
                lihat = csv.reader(file)
                next(lihat)

                total = 0
                file_found = False
                for baris in lihat:
                    if len(baris) < 4:
                        print("peringatan!, baris yang tidak valid akan di lewati")
                        continue
                    print(f"-{baris[0]}|{baris[1]}|{baris[2]}|{baris[3]}-")
                    total += float(baris[2])
                    file_found = True

                if not file_found:
                    print("belum ada pengeluaran tercatat!")
                else:    
                    print(f"total pengeluaran Rp.{total}")

        except FileNotFoundError:
            print("file tidak di temukan")
        except Exception as e:
            print(f"terjadi masalah saat membaca data: {e}")

if __name__ == "__main__":

    folder_pemasukan = "data_pemasukan"
    file_pemasukan = f"pemasukan_bulan({datetime.now().month}).csv"
    data_pemasukan = Struct(
            folder_pemasukan,
            file_pemasukan,
            "Waktu",
            "kategori",
            "Jumlah",
            "Jenis"
            )

    folder_pengeluaran = "data_pengeluaran"
    file_pengeluaran = f"pengeluaran_bulan({datetime.now().month}).csv"
    data_pengeluaran = Struct(
            folder_pengeluaran,
            file_pengeluaran,
            "Waktu",
            "kategori",
            "Jumlah",
            "Jenis"
            )

    catatan_finansial = FinancialTracker()
    try:
       
        while True:
            print("-------------------------------")
            print("1. =====TAMBAH PENGELUARAN=====")
            print("2. ======LIHAT PENGELUARAN=====")
            print("3. ======TAMBAH PEMASUKAN======")
            print("4. =======LIHAT PEMASUKAN======")
            print("5. ========EXIT PROGRAM========")
            print("-------------------------------\n")

            input_user = int(input("Masukkan angka (1-5) untuk memilih program: "))
            if input_user > 5 or input_user < 1:
                print("input tidak boleh lebih dari 5 dan kurang dari 1!")
                continue

            match input_user:
                case 1:
                    user_input: dict = {
                            "inp_hari": input("masukkan hari/tanggal ") or f"{datetime.now().date()}", # boleh di skip karna sudah otomatis terisi jika di skip
                        "inp_kategori": input("tambahkan kategori: "),
                        "inp_jumlah": float(input("masukkan jumlah: ").replace(".", "") or 0),
                        "inp_jenis": input("masukkan jenis: ")
                        } 

                    if user_input["inp_jumlah"] < 0:
                        print("jumlah tidak boleh kurang dari 0!")
                        continue
                    if not all(user_input.values()):
                        print("\ninput wajib di isi!")
                        continue

                    catatan_finansial.tambah_data(
                            Struct(
                                folder_pengeluaran,
                                file_pengeluaran,
                                user_input["inp_hari"],
                                user_input["inp_kategori"],
                                user_input["inp_jumlah"],
                                user_input["inp_jenis"]
                                )
                            )

                case 2:
                    catatan_finansial.lihat_data(data_pengeluaran)

                case 3:
                    user_input: dict = {
                        "inp_hari": input("masukkan hari/tanggal: ") or f"{datetime.now().date()}",
                        "inp_kategori": input("tambahkan kategori: "),
                        "inp_jumlah": float(input("masukkan jumlah: ").replace(".", "") or 0),
                        "inp_jenis": input("masukkan jenis: ")
                        } 
                    if user_input["inp_jumlah"] < 0:
                        print("jumlah tidak boleh kurang dari 0!")
                        continue
                    if not all(user_input.values()):
                        print("\ninput wajib di isi!")
                        continue

                    catatan_finansial.tambah_data(
                            Struct(
                                folder_pemasukan,
                                file_pemasukan,
                                user_input["inp_hari"],
                                user_input["inp_kategori"],
                                user_input["inp_jumlah"],
                                user_input["inp_jenis"]
                                )
                            )

                case 4:
                    catatan_finansial.lihat_data(data_pemasukan)

                case 5:
                    print("bye..")
                    exit(0)

    except Exception as e:
        print(f"telah terjadi error: {e}")
