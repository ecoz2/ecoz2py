#include <stdio.h>
#include "ecoz2_extension.h"

const char *ecoz2_version() {
  return "The ecoz2 version";
}

void ecoz2_baz(char* filename) {
  printf("C: ecoz2_baz: filename=%s\n", filename);
}

void ecoz2_do_filenames(char* filenames[], int num_filenames, callback_t callback) {
  for (int i = 0; i < num_filenames; ++i) {
    char* filename = filenames[i];
    printf("C: ecoz2_do_filenames: filenames[%d]=%s\n", i, filename);
    callback(filename, i);
  }
}
