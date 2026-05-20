import secrets
from string import ascii_letters, digits, punctuation
import os

def generate_pw(panjang: int) -> str:
    karakter = ascii_letters + digits + punctuation
    passwd = ''.join(secrets.choice(karakter) for _ in range(panjang))
    return passwd

def main() -> None:
    while True:
        print("====ALAT PEMBUAT PASSWORD====\n")

        try:
            panjang_pw: int = int(input("masukan berapa jumlah panjang password yang anda inginkan.\n(disarankan lebih dari 3): "))

            if panjang_pw <= 0:
                print("mikirkids, password tidak boleh kurang dari 0!,situ niat buat password apa nggak sih?\n")
                continue

            if panjang_pw <= 3:
                y_or_n: str = input("password terlalu pendek, apakah anda yakin? (y/n): ").lower()
                if y_or_n == 'y':
                    print("PASSWORD TELAH SUKSES DI BUAT!")
                    break
                elif y_or_n == 'n':
                    continue

                else:
                    print("input hanya boleh (y/n)!")
                    continue
            
            else:
                print("PASSWORD TELAH SUKSES DI BUAT!")
                break   
        
        except ValueError:
            print("input harus berupa angka!")
            continue

    show_pw = generate_pw(panjang_pw)
    print("="*30)
    print(f"password anda: {show_pw}")
    print("="*30)


if __name__ == '__main__':
    if os.name == 'posix':
        os.system("clear")
    else:
        os.system("cls")

    main()
    while True: 

        buat_lagi: str = input("apakah anda ingin membuat password lagi? (y/n): ").lower()
        if buat_lagi == 'y':
            main()
        elif buat_lagi == 'n':
            print("bye..")
            break

        else:
            print("input hanya boleh (y/n)!")
            continue
