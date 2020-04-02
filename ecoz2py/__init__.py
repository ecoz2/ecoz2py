from _ecoz2_extension import ffi
from _ecoz2_extension.lib import ecoz2_version
from _ecoz2_extension.lib import ecoz2_prd_show_file


def get_version():
    return ffi.string(ecoz2_version())


def prd_show_file(filename,
                  show_reflections=False,
                  from_=-1,
                  to=-1,
                  ):

    ecoz2_prd_show_file(filename, show_reflections, from_, to)
