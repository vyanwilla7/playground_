#include "sq.h"
#include <stdio.h>

int main(void){
  Squad sq[MAX_MEMBER];
  int index = 0;
  
  printf("\t\t=======data sq========\n");
  tambah_member(sq, &index, "Constance.", "jungler", 123);
  cari_data(sq,123);


  return 0;
}
