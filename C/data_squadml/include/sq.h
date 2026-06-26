#ifndef SQ_H
#define SQ_H

#define MAX_MEMBER 10

typedef struct{
  int id;
  char nick_name[15];
  char role[10];
} Squad;

void tambah_member(Squad sq[], int *arr, char *nick_name, char *role, int id);

void cari_data(const Squad sq[], int id);

void tampilkan_data(Squad sq[], int arr);
#endif // !SQ_H
