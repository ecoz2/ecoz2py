#
# export PYTHONPATH=.:ecoz2py
# python ecoz2_vq_learn_test.py
#
import ecoz2py as ecoz2
from ecoz2py import get_actual_filenames

USE_WANDB = False

print("USE_WANDB: {}".format(USE_WANDB))

if USE_WANDB:
    import wandb

print("ECOZ2 C version: {}".format(ecoz2.get_version()))

codebook_class_name = 'F'

predictor_filenames = get_actual_filenames(
    filenames=['../ecoz2-whale/exerc01/data/predictors/TRAIN/F'],
    file_ext='.prd'
)

if USE_WANDB:
    wandb.init(project="whale-vq")


def vq_learn_callback(variable, value):
    print("P: vq_learn_callback: variable={}, value={}".format(variable, value))
    if USE_WANDB:
        wandb.log({variable: value})


ecoz2.vq_learn(prediction_order=36,
               predictor_filenames=predictor_filenames,
               codebook_class_name=codebook_class_name,
               vq_learn_callback=vq_learn_callback)
