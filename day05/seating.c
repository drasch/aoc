#include <stdio.h>
#include "stb_ds.h"

int main( ) {

  char str[30];

  FILE* fp = fopen("input" , "r");

  if(fp == NULL) {
    perror("Error opening file");
    return(-1);
  }

  while (fgets(str, 20, fp) != NULL) {
    printf( "You entered: ");
    puts( str );
  }

  fclose(fp);
  return 0;
}
