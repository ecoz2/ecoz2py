const char *ecoz2_version();

void ecoz2_baz(char* filename);

typedef void (*callback_t)(char*, int);

void ecoz2_do_filenames(char* filenames[], int num_filenames, callback_t callback);
