from cffi import FFI
ffibuilder = FFI()

ffibuilder.cdef("""
const char *ecoz2_version();

const char *ecoz2_hi(const char *name);
int ecoz2_baz();

int ecoz2_prd_show_file(
        char *filename,
        int show_reflections,
        int from,
        int to
        );

typedef void (*callback_t)(char*, int);
void ecoz2_do_filenames(char* filenames[], int num_filenames, callback_t callback);

typedef void (*hmm_learn_callback_t)(char*, long double);

int ecoz2_hmm_learn(
        int N,
        int model_type,
        const char* sequence_filenames[],
        int num_sequences,
        double hmm_epsilon,
        double val_auto,
        int max_iterations,
        hmm_learn_callback_t callback
        );

""")

ffibuilder.set_source(
  "_ecoz2_extension",
  """
  #include "ecoz2_extension.h"
  #include "ecoz2.h"
  #include "lpc.h"
  """,
  include_dirs=[
    "../ecoz2/src/include"
  ],
  sources=[
    'ecoz2_extension.c',
    '../ecoz2/src/ecoz/ecoz2.c',
    '../ecoz2/src/utl/utl.c',
    '../ecoz2/src/utl/fileutil.c',
    '../ecoz2/src/utl/list.c',
    '../ecoz2/src/utl/memutil.c',
    '../ecoz2/src/sgn/sgn.c',
    '../ecoz2/src/sgn/dr_wav.c',
    '../ecoz2/src/lpc/lpc_signals.c',
    '../ecoz2/src/lpc/lpaOnSignal.c',
    '../ecoz2/src/lpc/lpca.c',
    '../ecoz2/src/lpc/prd.c',
    '../ecoz2/src/lpc/prd_show_file.c',
    '../ecoz2/src/lpc/ref2raas.c',
    '../ecoz2/src/vq/vq_learn.c',
    '../ecoz2/src/vq/vq_quantize.c',
    '../ecoz2/src/vq/vq_classify.c',
    '../ecoz2/src/vq/vq_show.c',
    '../ecoz2/src/vq/vq.c',
    '../ecoz2/src/vq/distortion.c',
    '../ecoz2/src/vq/report.c',
    '../ecoz2/src/vq/sigma.c',
    '../ecoz2/src/vq/inertia.c',
    '../ecoz2/src/vq/quantize.c',
    '../ecoz2/src/hmm/hmm.c',
    '../ecoz2/src/hmm/hmm_learn.c',
    '../ecoz2/src/hmm/hmm_classify.c',
    '../ecoz2/src/hmm/hmm_show.c',
    '../ecoz2/src/hmm/seq_show_files.c',
    '../ecoz2/src/hmm/hmm_adjustb.c',
    '../ecoz2/src/hmm/hmm_file.c',
    '../ecoz2/src/hmm/hmm_refinement.c',
    '../ecoz2/src/hmm/hmm_log_prob.c',
    '../ecoz2/src/hmm/hmm_genQopt.c',
    '../ecoz2/src/hmm/hmm_estimateB.c',
    '../ecoz2/src/hmm/hmm_gen.c',
    '../ecoz2/src/hmm/distr.c',
    '../ecoz2/src/hmm/symbol.c',
  ],
  libraries=[]
)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
