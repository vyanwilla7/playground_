#include <stdio.h>

#define SIZE 5

void tampilkan_hasil(int *p){
  for (int i = 0; i < SIZE; i++){
    printf("%d ", p[i]);
  }
}

int main(void){

  int arr[SIZE] = {40, 20, 10, 50, 30};

  for (int i = 0; i < SIZE - 1; i++){
    int min_index = i;

    for (int j = i + 1; j < SIZE; j++){
      if (arr[j] < arr[min_index]){
        min_index = j;
      }
    }
    if (min_index != i){
      int x = arr[i];
      arr[i] = arr[min_index];
      arr[min_index] = x;
    }
  }

  tampilkan_hasil(arr);

  return 0;
}
