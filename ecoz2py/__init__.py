from _ecoz2_extension import ffi
from _ecoz2_extension.lib import ecoz2_version
from _ecoz2_extension.lib import ecoz2_prd_show_file
from _ecoz2_extension.lib import ecoz2_set_random_seed
from _ecoz2_extension.lib import ecoz2_hmm_learn


def get_version():
    return ffi.string(ecoz2_version())


def prd_show_file(filename,
                  show_reflections=False,
                  from_=-1,
                  to=-1,
                  ):

    ecoz2_prd_show_file(filename, show_reflections, from_, to)


def to_bytes(s):
    return s if isinstance(s, bytes) else str(s).encode("utf-8")


def to_str(s):
    return s if isinstance(s, str) else bytes(s).decode("utf-8")


def set_random_seed(seed):
    ecoz2_set_random_seed(seed)


def hmm_learn(N,
              sequence_filenames,
              model_type=3,
              hmm_epsilon=1.e-5,
              val_auto=0.3,
              max_iterations=-1,
              hmm_learn_callback=None
              ):

    c_sequence_filenames_keepalive = [ffi.new("char[]", to_bytes(s)) for s in sequence_filenames]
    c_sequence_filenames = ffi.new("char *[]", c_sequence_filenames_keepalive)

    # for (i, c_sequence_filename) in enumerate(c_sequence_filenames):
    #     print('SEQ {} => {}'.format(i, ffi.string(c_sequence_filename)))

    @ffi.callback("void(char*, double)")
    def callback(c_variable, c_value):
        if hmm_learn_callback:
            variable = to_str(ffi.string(c_variable))
            value = float(c_value)
            hmm_learn_callback(variable, value)

    ecoz2_hmm_learn(N,
                    model_type,
                    c_sequence_filenames,
                    len(c_sequence_filenames),
                    hmm_epsilon,
                    val_auto,
                    max_iterations,
                    callback
                    )
