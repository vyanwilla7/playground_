from qr_gen import QRGenerator

def main() -> None:
    print("==== QR Generator ====")
    while True:
        data: str = input("Masukkan url/link/text: ")
        warna_qr: str = input("Pilih warna, [default: white]: ") or "white"
        background_qr: str = input("Pilih warna background, [default: black]: ") or "black"

        try:
            ukuran: int = int(input("Masukkan ukuran QR [10]: ")) or 10
            ukuran: int = int(ukuran) if ukuran else 10
        except ValueError:
            print("QR belum dapat di generate")
            continue

        nama_file: str = input("Buat nama file, [default: qrcode]: ") or "qrcode"

        qr = QRGenerator(
                data = data,
                fill=warna_qr,
                back=background_qr,
                size=ukuran
                )
        qr.generate()

        tambah_logo: str = input("Apakah anda akan menambahkan logo dalam QR anda? (y/n): ").lower()
        if tambah_logo == 'y':
            path_logo: str = input("Masukkan path: ")
            qr.add_logo(path_logo)

        elif tambah_logo == 'n':
            print("okee..")

        else:
            print("input tidak valid!, hanya boleh y/n")
            continue

        path = qr.save_qr(nama_file)
        print(f"\nQR telah sukses dibuat!")
        print(f"lokasi file: {path}")


        lagi: str = input("Apakah anda ingin membuat QR Code lagi? (y/n): ").lower()

        if lagi == 'y':
            continue
        elif lagi == 'n':
            print("bye...")
            break
        else:
            print("input tidak valid!")
            continue

if __name__ == "__main__":
    main()
