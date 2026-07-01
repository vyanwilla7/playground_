#include "kalkulator.h"
#include <stdio.h>
#include <stdbool.h>

int main(void){
  printf("\t=====KALKULATOR SEDERHANA=====\n");
  while (true){

    int pilih_operator; 
    printf("\tpilih operator: ");scanf("%d", &pilih_operator);

    if (pilih_operator == 0){
      printf("\tbye...\n");
      break;
    }

    if (pilih_operator < 0 || pilih_operator > 4){
      fprintf(stderr, "\tinput tidak valid!\n");
      continue;
    }
    float angka1, angka2;

    printf("\tmasukkan angka pertama: ");
    scanf("%f", &angka1);

    printf("\tmasukkan angka kedua: ");
    scanf("%f", &angka2);

    switch (pilih_operator) {
      case 1:
        printf("\t<=========================>\n");
        printf("\thasil penjumlahan: %.2f\n", tambah(angka1, angka2));
        printf("\t<=========================>\n");

        break;

      case 2:
        printf("\t<=========================>\n");
        printf("\thasil pengurangan: %.2f\n", kurang(angka1, angka2));
        printf("\t<=========================>\n");

        break;

      case 3:
        printf("\t<=========================>\n");
        printf("\thasil perkalian: %.2f\n", kali(angka1, angka2));
        printf("\t<=========================>\n");

        break;

      case 4:
        if (angka2 == 0){
          fprintf(stderr, "\tangka kedua != 0!\n");
          continue;
        }
        printf("\t<=========================>\n");
        printf("\thasil pembagian: %.2f\n", bagi(angka1, angka2));
        printf("\t<=========================>\n");

        break;

      default:
        printf("\tinput tidak valid!\n");

    }

  }
  return 0;
}
