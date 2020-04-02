#include <stdio.h>
#include "ecoz2_extension.h"
#include "ecoz2.h"

void ecoz2_do_filenames(char* filenames[], int num_filenames, callback_t callback) {
  for (int i = 0; i < num_filenames; ++i) {
    char* filename = filenames[i];
    printf("C: ecoz2_do_filenames: filenames[%d]=%s\n", i, filename);
    callback(filename, i);
  }
}
