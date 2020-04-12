// contents of this file copied from ../ecoz2/src/include/ecoz2.h
// but without directives, apparently not supported.

const char *ecoz2_version();

void ecoz2_set_random_seed(int seed);

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

typedef void (*vq_learn_callback_t)(char*, double);

int ecoz2_vq_learn(
        int prediction_order,
        double epsilon,
        const char *codebook_class_name,
        const char *predictor_filenames[],
        int num_predictors,
        vq_learn_callback_t callback
        );
