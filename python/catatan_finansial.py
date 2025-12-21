import os
import csv
import pyfiglet

class CatatanFinansial:
    def __init__(self, tanggal, kategori, jumlah):
        self.tanggal = tanggal
        self.kategori = kategori
        self.jumlah = jumlah

class Pengeluaran(CatatanFinansial):
    def __init__(self, tanggal, kategori, jumlah):
        super().__init__(tanggal, kategori, jumlah)

    def to_csv_row(self):
        return [self.tanggal, self.kategori, self.jumlah]

class Pemasukan(CatatanFinansial):
    def __init__(self, tanggal, kategori, jumlah):
        super().__init__(tanggal, kategori, jumlah)
    
    def to_csv_row(self):
        return [self.tanggal, self.kategori, self.jumlah]
    
class ManageCSV:
    def __init__(self, FILE_NAME, header):
        self.__nama_file = FILE_NAME
        self.__head = header
        self.__init__file()
        
    def __init__file(self):
        if not os.path.exists(self.__nama_file):
            with open(self.__nama_file, 'w', newline='') as files:
                writter = csv.writer(files)
                writter.writerow(self.__head)

    def tambah_pengeluaran_dan_pemasukan(self, records):
        try:
            with open(self.__nama_file, 'a', newline='') as   files:
                writter = csv.writer(files)
                writter.writerow(records.to_csv_row())
            print("\ndata berhasil di tambahkan!")

        except Exception as e:
            print(f"Gagal menyimpan data, terjadi error: {e}")

    def lihat_pengeluaran_dan_pemasukan(self):
        try:
            with open(self.__nama_file, 'r') as files:
                lihat = csv.reader(files)
                next(lihat)

                total = 0
                file_found = False
                for row in lihat:
                    if len(row) < 3:
                        print("Peringatan!, baris tidak valid akan dilewati.")
                        continue
                    print(f"-{row[0]}|{row[1]}|{row[2]}")
                    total += float(row[2])
                    file_found = True
            if not file_found:
                print("belum ada pengeluaran tercatat!")
            else:
                print(f"total pengeluaran Rp: {total}")
        except FileNotFoundError:
            print("file tidak di temukan!")
        except Exception as e:
            print(f"terjadi masalah saat membaca data: {e}")

if __name__ == '__main__':

    pemasukan_csv = ManageCSV(
        'Pemasukan.csv',
        ['Tanggal', 'Kategori', 'Jumlah']        
    )
    pengeluaran_csv = ManageCSV(
        'Pengeluaran.csv',
        ['Tanggal', 'Kategori', 'Jumlah']
    )

    try:
        judul = pyfiglet.figlet_format("\nCATATAN FINANSIAL\n")
        print(judul)

        while True:
            print("-------------------------------")
            print("1. =====TAMBAH PENGELUARAN=====")
            print("2. ======LIHAT PENGELUARAN=====")
            print("3. ======TAMBAH PEMASUKAN======")
            print("4. =======LIHAT PEMASUKAN======")
            print("5. ========EXIT PROGRAM========")
            print("-------------------------------\n")

            input_user = int(input("Masukkan angka (1-5) untuk memilih program: "))

            match input_user:
                case 1:

                    tanggal = input("Masukkan tanggal(DD/MM/YYYY): ")
                    kategori = input("Masukkan kategori: ")

                    if not tanggal:
                        print("Tanggal wajib di isi!, tidak boleh kosong.")
                    if not kategori:
                        print("Kategori wajib di isi!, tidak boleh kosong.")

                    try:
                        jumlah = float(input("Masukkan jumlah: ").replace('.', ''))
                    except ValueError:
                        print("Input tidak valid!, harus berupa angka")

                    if jumlah < 0:
                        print("Jumlah tidak boleh < 0")
                        

                    pengeluaran_csv.tambah_pengeluaran_dan_pemasukan(
                        Pengeluaran(tanggal, kategori, jumlah)
                    )
                

                case 2:
                    pengeluaran_csv.lihat_pengeluaran_dan_pemasukan()
                
                case 3:            
                    tanggal = input("Masukkan tanggal(DD/MM/YYYY): ")
                    kategori = input("Masukkan kategori: ")

                    if not tanggal:
                        print("Tanggal wajib di isi!, tidak boleh kosong.")
                    if not kategori:
                        print("Kategori wajib diisi!, tidak boleh kosong.")                 
                    try:
                        jumlah = float(input("Masukkan jumlah: ").replace('.', ''))
                    except ValueError:
                        print("Input tidak valid!, harus berupa angka.")
                    
                    if jumlah < 0:
                        print("jumlah tidak boleh < 0")
                        continue

                    pemasukan_csv.tambah_pengeluaran_dan_pemasukan(
                        Pemasukan(tanggal, kategori, jumlah)
                    )
                    
                case 4:
                    pemasukan_csv.lihat_pengeluaran_dan_pemasukan()

                case 5:
                    keluar = pyfiglet.figlet_format("Terimakasih telah menggunakan program ini:)", font='small')
                    print(keluar)
                    
                    exit()
                
                case _:
                    print("input tidak valid, coba lagi!")
                    continue
    except ZeroDivisionError:
        print("Input tidak boleh = 0!")
