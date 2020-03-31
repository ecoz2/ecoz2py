cdef extern from "ecoz2.h":
    const char *ecoz2_version()
    const char *ecoz_foo(const char *name)

    int ecoz2_lpc_signals(
        int p,
        int window_length_ms,
        int offset_length_ms,
        int minpc,
        float split,
        char *sgn_filenames[],
        int num_signals
        )

    int ecoz2_prd_show_file(
      char *filename,
      bint show_reflections,
      int from_,
      int to)

def version() -> bytes:
    return ecoz2_version()

def foo(name: bytes) -> bytes:
    return ecoz_foo(name)

def lpc_signals(p: int,
                window_length_ms: int,
                offset_length_ms: int,
                minpc: int,
                split: float,
                sgn_filenames: [bytes],
                num_signals: int
                ):
    return ecoz2_lpc_signals(p,
                             window_length_ms,
                             offset_length_ms,
                             minpc,
                             split,
                             sgn_filenames,
                             num_signals)

def prd_show_file(filename: bytes, show_reflections: bool, from_: int, to: int):
    return ecoz2_prd_show_file(filename, show_reflections, from_, to)
