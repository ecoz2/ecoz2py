from cffi import FFI
ffibuilder = FFI()

ffibuilder.cdef("""
const char *ecoz2_version();
void ecoz2_baz(char* filename);

typedef void (*callback_t)(char*, int);
void ecoz2_do_filenames(char* filenames[], int num_filenames, callback_t callback);
""")

ffibuilder.set_source("_ecoz2_extension",  # name of the output C extension
"""
    #include "ecoz2_extension.h"
""",
    sources=['ecoz2_extension.c'],   # includes ecoz2_extension.c as additional sources
    libraries=['m'])                 # on Unix, link with the math library

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
