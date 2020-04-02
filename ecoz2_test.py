#
# export PYTHONPATH=.:ecoz2py
# python ecoz2_test.py
#
import ecoz2py as ecoz2

print("ECOZ2 C version: {}".format(ecoz2.get_version()))

ecoz2.prd_show_file(
  b"../ecoz2-whale/exerc01/data/predictors/TRAIN/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__10079.092_10080.35.prd"
)
