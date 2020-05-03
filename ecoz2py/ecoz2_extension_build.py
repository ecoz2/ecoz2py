import os

from cffi import FFI

ffibuilder = FFI()

with open(os.path.join(os.path.dirname(__file__), 'ecoz2_extension.h')) as f:
    ffibuilder.cdef(f.read())

ffibuilder.set_source(
  module_name="_ecoz2_extension",
  source="""
  #include "ecoz2_extension.h"
  #include "ecoz2.h"
  #include "lpc.h"
  """,
  include_dirs=[
    "../ecoz2/src/include"
  ],
  extra_compile_args=['-fopenmp'],
  extra_link_args=['-fopenmp'],
  sources=[
    '../ecoz2/src/ecoz2/ecoz2.c',
    '../ecoz2/src/utl/utl.c',
    '../ecoz2/src/utl/fileutil.c',
    '../ecoz2/src/utl/list.c',
    '../ecoz2/src/utl/memutil.c',
    '../ecoz2/src/sgn/sgn.c',
    '../ecoz2/src/sgn/dr_wav.c',
    '../ecoz2/src/lpc/lpc_signals.c',
    '../ecoz2/src/lpc/lpa_on_signal.c',
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
    # '../ecoz2/src/hmm/hmm_refinement.c',
    '../ecoz2/src/hmm/hmm_prob.c',
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
