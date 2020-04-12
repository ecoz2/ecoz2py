from _ecoz2_extension import ffi
from _ecoz2_extension.lib import ecoz2_version
from _ecoz2_extension.lib import ecoz2_prd_show_file
from _ecoz2_extension.lib import ecoz2_hmm_learn

print("ECOZ2 C version: {}".format(ffi.string(ecoz2_version())))

ecoz2_prd_show_file(
  b"../../ecoz2-whale/exerc01/data/predictors/TRAIN/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__10079.092_10080.35.prd",
  0, -1, -1
)


def to_bytes(s):
    return s if isinstance(s, bytes) else str(s).encode("utf-8")


####################################################

@ffi.callback("void(char*, double)")
def hmm_learn_callback(c_variable, c_value):
    variable = ffi.string(c_variable)
    value = float(c_value)
    print("P: hmm_learn_callback: variable={}, c_value={}, value={}".format(variable, c_value, value))


sequence_filenames = [
  '../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__10079.092_10080.35.seq',
  '../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__10540.822_10543.197.seq',
  '../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__1068.8552_1069.205.seq',
  '../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__1089.723_1090.6355.seq',
  '../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__12907.783_12909.293.seq',
  '../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__15415.037_15417.307.seq',
  '../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__2926.575_2929.6223.seq',
  '../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__5067.5444_5070.2764.seq',
  '../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__588.77454_591.3191.seq',
  '../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__680.14154_680.8046.seq',
  '../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__7145.495_7147.0107.seq',
]

# see https://cffi.readthedocs.io/en/latest/using.html#an-example-of-calling-a-main-like-thing
c_sequence_filenames_keepalive = [ffi.new("char[]", to_bytes(s)) for s in sequence_filenames]
c_sequence_filenames = ffi.new("char *[]", c_sequence_filenames_keepalive)

ecoz2_hmm_learn(
  8,  # N
  3,  # model_type: HMM_CASCADE3
  c_sequence_filenames,
  len(c_sequence_filenames),
  1.e-5,  #  hmm_epsilon,
  0.3,    #  val_auto,
  -1,     # max_iterations,
  hmm_learn_callback
)
