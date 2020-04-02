from _ecoz2_extension import ffi
from _ecoz2_extension.lib import ecoz2_version, ecoz2_baz, ecoz2_hi
from _ecoz2_extension.lib import ecoz2_prd_show_file
from _ecoz2_extension.lib import ecoz2_hmm_learn
from _ecoz2_extension.lib import ecoz2_do_filenames

print("ECOZ2 C version: {}".format(ffi.string(ecoz2_version())))

print("ecoz2_baz = {}".format(ecoz2_baz()))

print("ecoz2_hi('calvin') = {}".format(ffi.string(ecoz2_hi(b'calvin'))))

# filenames = [
#   b"somefile1.txt",
#   b"somefile2.txt",
#   b"somefile3.txt",
# ]
# buffer_in = ffi.new("char*[]", len(filenames))
# for (i, filename) in enumerate(filenames):
#     buffer_in[i] = ffi.new("char[]", filename)
#
#
# @ffi.callback("void(char*, int)")
# def myfunc(c_filename, i):
#     filename = ffi.string(c_filename)
#     print("P: myfunc: filename={}, i={}".format(filename, i))
#
#
# ecoz2_do_filenames(buffer_in, len(filenames), myfunc)
#
# ecoz2_prd_show_file(
#   b"../../ecoz2-whale/exerc01/data/predictors/TRAIN/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__10079.092_10080.35.prd",
#   0, -1, -1
# )


####################################################

@ffi.callback("void(char*, long double)")
def hmm_learn_callback(c_variable, c_value):
    variable = ffi.string(c_variable)
    value = float(c_value)
    print("\nP: hmm_learn_callback: variable={}, c_value={}, value={}\n".format(variable, c_value, value))


sequence_filenames = [
  b'../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__10079.092_10080.35.seq',
  b'../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__10540.822_10543.197.seq',
  b'../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__1068.8552_1069.205.seq',
  b'../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__1089.723_1090.6355.seq',
  b'../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__12907.783_12909.293.seq',
  b'../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__15415.037_15417.307.seq',
  b'../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__2926.575_2929.6223.seq',
  b'../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__5067.5444_5070.2764.seq',
  b'../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__588.77454_591.3191.seq',
  b'../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__680.14154_680.8046.seq',
  b'../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__7145.495_7147.0107.seq',
]
c_sequence_filenames = ffi.new("char*[]", len(sequence_filenames))
for (i, filename) in enumerate(sequence_filenames):
    c_sequence_filenames[i] = ffi.new("char[]", filename)
    print('c_sequence_filenames[{}] = {}'.format(i, ffi.string(c_sequence_filenames[i])))


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

