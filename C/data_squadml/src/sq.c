#include "sq.h"
#include <stdio.h>
#include <string.h>

void tambah_member(Squad sq[], int *arr, char *nick_name, char *role, int id){
  if (*arr >= MAX_MEMBER){
fprintf(stderr, "error: jumlah melebihi batas!\n");
    return;
  }
  sq[*arr].id = id;
  strncpy(sq[*arr].nick_name, nick_name, 15 - 1);
  sq[*arr].nick_name[15 - 1] = '\0';
  strncpy(sq[*arr].role, role, 10 - 1);
  sq[*arr].role[10 - 1] = '\0';

  printf("data berhasil di tambahkan!\n");
  (*arr)++;
}

void cari_data(const Squad sq[], int id){
  for (int i = 0; i < MAX_MEMBER; i++){
    if (id == sq[i].id){
      printf("\ndata di temukan!\n");
      printf("\n=========info data=========\n");
      printf("nick_name: %s||role: %s\n", sq[i].nick_name, sq[i].role);

      return;

    }
  }
  fprintf(stderr, "error: data tidak di temukan!\n");
}

void tampilkan_data(Squad sq[], int arr){
  if (arr == 0){
    fprintf(stderr, "data masih kosong!\n");
    return;
  }

  for (int i = 0; i < arr; i++){
    printf("nick_name: %s||role: %s||id: %d\n", sq[i].nick_name, sq[i].role, sq[i].id);
  }
}
