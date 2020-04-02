#
# export PYTHONPATH=.:ecoz2py
# python ecoz2_test.py
#
from ecoz2py import ecoz2_get_version
from ecoz2py import ecoz2_prd_show_file

print("VERSION: {}".format(ecoz2_get_version()))

ecoz2_prd_show_file(
  b"../ecoz2-whale/exerc01/data/predictors/TRAIN/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__10079.092_10080.35.prd"
)
