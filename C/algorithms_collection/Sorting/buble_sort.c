#include <stdio.h>

void hasil(int *p){
  for (int i = 0; i < 5; i++) {
    printf("%d ", p[i]);
  }
}

int main(void){

  int arr[5] = {4,3,5,2,1};

  for (int i = 0; i < 5; i++){
    for (int j = 0; j < 5 - i - 1; j++){
      if (arr[j] > arr[j + 1]){
        int x = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = x;
      }
    }
  }

  hasil(arr);
  return 0;
}
