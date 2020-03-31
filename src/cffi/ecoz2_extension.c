#include <stdio.h>

const char *ecoz2_version() {
  return "The ecoz2 version";
}

void ecoz2_baz(char* filename) {
  printf("From-C: ecoz2_baz: filename=%s\n", filename);
}

void ecoz2_do_filenames(char* filenames[], int num_filenames) {
  for (int i = 0; i < num_filenames; ++i) {
    printf("From-C: ecoz2_do_filenames: filenames[%d]=%s\n", i, filenames[i]);
  }
}
