#include <stdio.h>
#include <string.h>

const unsigned int FLAG_LEN = 26;

void reset_flags_and_increment(unsigned int * flags, unsigned int * sum, int record_group) {
  for (int i=0; i < FLAG_LEN; i++) {
    if (flags[i] == record_group) {
      *sum += 1;
    }
    flags[i] = 0;
  }
}


int main( ) {
  unsigned int flags[FLAG_LEN];
  char buf[FLAG_LEN*2];
  unsigned int sum;
  unsigned int record_group = 0;

  FILE* fp = fopen("input" , "r");

  if(fp == NULL) {
    perror("Error opening file");
    return(-1);
  }

  // reset flags
  reset_flags_and_increment(flags, &sum, 9999);
  sum = 0;

  while (fgets(buf, FLAG_LEN*2-1, fp) != NULL) {
    if (strlen(buf) == 0 || buf[0] == '\n') {
      reset_flags_and_increment(flags, &sum, record_group);
      record_group = 0;
    }
    else if (strlen(buf) > 0) {
      int i = 0;
      while (buf[i] != '\n' && i < strlen(buf)) {
        int pos = buf[i] - 'a';
        if (pos >= 0 && pos < FLAG_LEN) {
          flags[pos] += 1;
        }
        i++;
      }
      record_group++;
    }
  }
  reset_flags_and_increment(flags, &sum, record_group);

  printf("%d\n", sum);

  fclose(fp);
  return 0;
}
