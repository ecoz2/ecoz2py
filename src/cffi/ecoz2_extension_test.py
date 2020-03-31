from _ecoz2_extension import ffi
from _ecoz2_extension.lib import ecoz2_version, ecoz2_baz, ecoz2_do_filenames

print(ffi.string(ecoz2_version()))

ecoz2_baz(b"somefile.txt")

filenames = [
  b"somefile1.txt",
  b"somefile2.txt",
  b"somefile3.txt",
]
buffer_in = ffi.new("char*[]", len(filenames))
for (i, filename) in enumerate(filenames):
    buffer_in[i] = ffi.new("char[]", filename)

ecoz2_do_filenames(buffer_in, len(filenames))
