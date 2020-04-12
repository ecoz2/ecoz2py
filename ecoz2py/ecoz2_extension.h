// contents of this file copied from ../ecoz2/src/include/ecoz2.h
// but without directives, apparently not supported.

const char *ecoz2_version();

// for test purposes
const char *ecoz2_hi(const char *name);
int ecoz2_baz();


int ecoz2_lpc_signals(
        int P,
        int windowLengthMs,
        int offsetLengthMs,
        int minpc,
        float split,
        char *sgn_filenames[],
        int num_signals
        );

int ecoz2_prd_show_file(
        char *filename,
        int show_reflections,
        int from,
        int to
        );

typedef void (*hmm_learn_callback_t)(char*, double);

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

