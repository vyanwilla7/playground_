#include <stdio.h>

#define SIZE 5

void tampilkan_hasil(int *p){
  for (int i = 0; i < SIZE; i++){
    printf("%d ", p[i]);
  }
}

int main(void){

  int arr[SIZE] = {40, 20, 50, 10, 30};

  for (int i = 1; i < SIZE; i++){
    int x = arr[i];
    int j = i - 1;

    while (j >= 0 && arr[j] > x){
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = x;
  }

  tampilkan_hasil(arr);

  return 0;
}
