from _ecoz2_extension import ffi
from _ecoz2_extension.lib import ecoz2_version, ecoz2_baz, ecoz2_do_filenames
from _ecoz2_extension.lib import prd_show_file


def ecoz2_get_version():
    return ffi.string(ecoz2_version())


# print("VERSION: {}".format(ecoz2_get_version()))


def ecoz2_prd_show_file(filename,
                        show_reflections=False,
                        from_=-1,
                        to=-1,
                        ):
    prd_show_file(filename, show_reflections, from_, to)


# ecoz2_prd_show_file(
#   b"../../ecoz2-whale/exerc01/data/predictors/TRAIN/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__10079.092_10080.35.prd"
# )
