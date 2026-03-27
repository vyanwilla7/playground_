#include <iostream>
#include <stdexcept> // Untuk error input
#include <string>

using namespace std;

void pembukaan() {
    char masuk;
    cout << "Apakah anda ingin memulai program ini? (y/n): ";
    cin >> masuk;

    if (masuk == 'y') {
        cout << "<=====================================>" << endl;
        cout << "SELAMAT DATANG DI KALKULATOR SEDERHANA!" << endl;
        return;

    } else (masuk != 'y'); {
        cout << "Ok, gua cabut" << endl;
        exit(0);
    }
}

void input_program() {
    // Looping menggunakan while true
    
    while (true) {
        
        cout << "<=====================================>" << endl;
        cout << "1. Penjumlahan" << endl;
        cout << "2. Pengurangan" << endl;
        cout << "3. Perkalian"   << endl;
        cout << "4. Pembagian"   << endl;
        cout << "5. Exit program"<< endl;
        cout << "<=====================================>" << endl;
        
        /* Disini gua mau make logika if else yang akan masuk
           dalam try catch dengan tujuan agar krtika pemain
           memasukan huruf akan ada peringatan.             */

        try {
            int pilih_operator;
            cout << "Silahkan pilih operator program anda:";
            cin >> pilih_operator;
            
            if (pilih_operator == 1) {
                int angka1_penjumlahan, angka2_penjumlahan;
                
                cout << "Masukkan angka pertama: ";
                cin >> angka1_penjumlahan;
                cout << "Masukkan angka kedua: ";
                cin >> angka2_penjumlahan;

                cout << "<=====================================>" << endl;
                cout << "Hasil dari " << angka1_penjumlahan << " + " << angka2_penjumlahan << " Adalah:"; 
                cout << (angka1_penjumlahan + angka2_penjumlahan) << endl;     
                
            } else if (pilih_operator == 2){ 
                int angka1_pengurangan, angka2_pengurangan;
                
                cout << "Masukkan angka pertama: ";
                cin >> angka1_pengurangan;
                cout << "Masukkan angka kedua: ";
                cin >> angka2_pengurangan;
                
                cout << "<=====================================>" << endl;
                cout << "Hasil dari " << angka1_pengurangan << " - " << angka2_pengurangan << " Adalah:"; 
                cout << (angka1_pengurangan - angka2_pengurangan) << endl;     
                
            } else if (pilih_operator == 3){
                int angka1_perkalian, angka2_perkalian;
                
                cout << "Masukkan angka pertama: ";
                cin >> angka1_perkalian;
                cout << "Masukkan angka kedua: ";
                cin >> angka2_perkalian;
                
                cout << "<=====================================>" << endl;
                cout << "Hasil dari " << angka1_perkalian << " * " << angka2_perkalian << " Adalah:"; 
                cout << (angka1_perkalian * angka2_perkalian) << endl;     
                
            } else if (pilih_operator == 4){
                
                int angka1_pembagian, angka2_pembagian;
                
                cout << "Masukkan angka pertama: ";
                cin >> angka1_pembagian;
                cout << "Masukkan angka kedua: ";
                cin >> angka2_pembagian;
                
                cout << "<=====================================>" << endl;
                cout << "Hasil dari " << angka1_pembagian << " / " << angka2_pembagian << " Adalah:"; 
                cout << (angka1_pembagian / angka2_pembagian) << endl;     

            } else if (pilih_operator < 5 or pilih_operator >5) {
                cout << "Input tidak valid, coba lagi!" << endl;
                continue;

            } else {
                cout << "Exit program" << endl;
                break;
            }

            // Banyak banget kalo make if else, tau gitu tadi gua make switch case aja ya.
            
    } 
        catch (const runtime_error& e) {
            cerr << "Input harus berupa angka!" << e.what() << endl; 
            continue;
    }
}
}

// Eksekusi
int main() {
    pembukaan();
    input_program();

    return 0;
}