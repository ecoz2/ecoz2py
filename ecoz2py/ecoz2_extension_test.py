from _ecoz2_extension import ffi
from _ecoz2_extension.lib import ecoz2_version, ecoz2_baz, ecoz2_hi
from _ecoz2_extension.lib import ecoz2_prd_show_file
from _ecoz2_extension.lib import ecoz2_do_filenames

print("ECOZ2 C version: {}".format(ffi.string(ecoz2_version())))

print("ecoz2_baz = {}".format(ecoz2_baz()))

print("ecoz2_hi('calvin') = {}".format(ffi.string(ecoz2_hi(b'calvin'))))

filenames = [
  b"somefile1.txt",
  b"somefile2.txt",
  b"somefile3.txt",
]
buffer_in = ffi.new("char*[]", len(filenames))
for (i, filename) in enumerate(filenames):
    buffer_in[i] = ffi.new("char[]", filename)


@ffi.callback("void(char*, int)")
def myfunc(c_filename, i):
    filename = ffi.string(c_filename)
    print("P: myfunc: filename={}, i={}".format(filename, i))


ecoz2_do_filenames(buffer_in, len(filenames), myfunc)

ecoz2_prd_show_file(
  b"../../ecoz2-whale/exerc01/data/predictors/TRAIN/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__10079.092_10080.35.prd",
  0, -1, -1
)
