#include "kalkulator.h"
#include <stdio.h>
#include <stdbool.h>

int main(void){
  printf("=====KALKULATOR SEDERHANA=====\n");
  while (true){

    int pilih_operator; 
    printf("DAFTAR OPERATOR:\n");
    printf("\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n0. Exit\n");
    printf("<============================>\n");
    printf("pilih operator: ");
    scanf("%d", &pilih_operator);

    if (pilih_operator == 0){
      printf("\tbye...\n");
      break;
    }

    if (pilih_operator < 0 || pilih_operator > 4){
      fprintf(stderr, "input tidak valid!\n");
      continue;
    }
    float angka1, angka2;

    printf("masukkan angka pertama: ");
    scanf("%f", &angka1);

    printf("masukkan angka kedua: ");
    scanf("%f", &angka2);

    switch (pilih_operator) {
      case 1:
        printf("<=========================>\n");
        printf("hasil penjumlahan: %.2f\n", tambah(angka1, angka2));
        printf("<=========================>\n");

        break;

      case 2:
        printf("<=========================>\n");
        printf("hasil pengurangan: %.2f\n", kurang(angka1, angka2));
        printf("<=========================>\n");

        break;

      case 3:
        printf("<=========================>\n");
        printf("hasil perkalian: %.2f\n", kali(angka1, angka2));
        printf("<=========================>\n");

        break;

      case 4:
        if (angka2 == 0){
          fprintf(stderr, "angka kedua != 0!\n");
          continue;
        }
        printf("<=========================>\n");
        printf("hasil pembagian: %.2f\n", bagi(angka1, angka2));
        printf("<=========================>\n");

        break;

      default:
        printf("input tidak valid!\n");

    }

  }
  return 0;
}
