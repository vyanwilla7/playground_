from qr_gen import QRGenerator

def main() -> None:
    print("\n==== QR GENERATOR ====")

    data: str = input("Masukkan url/text: ")

    fill: str = input("Masukkan warna [white]: ") or "white"

    back: str = input("Masukkan backgraund [black]: ") or "black"

    try:
        size: int = int(input("Masukkan ukuran QR [10]: ")or 10)
    except ValueError:
        print("\ninput harus berupa angka, coba lagi!")
        return

    file_name: str = input("Buat nama file [qrcode]: ") or "qrcode"

    qr = QRGenerator(
            data = data,
            fill = fill,
            back = back,
            size = size
            )
    qr.generate()

   
    tambah_logo: str = input("apakah anda ingin menambahkan logo dalam QR anda? (y/n)").lower()

    if tambah_logo == 'y':
        path = input("masukkan path: ")
        qr.add_logo(path)

    path = qr.save_qr(file_name)
    print("\n QR telah sukses dibuat!")
    print(f"lokasi file: {path}")
if __name__ == "__main__":
    main()
