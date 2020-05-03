#
# export PYTHONPATH=.:ecoz2py
# python ecoz2_hmm_learn_test.py
#
import ecoz2py as ecoz2
from ecoz2py import get_actual_filenames

USE_WANDB = False

print("USE_WANDB: {}".format(USE_WANDB))

if USE_WANDB:
    import wandb

print("ECOZ2 C version: {}".format(ecoz2.get_version()))

sequence_filenames = get_actual_filenames(
    filenames=['ecoz2py/data/sequences/TRAIN/M1024/B'],
    file_ext='.seq'
)

if USE_WANDB:
    wandb.init(project="whale")


def hmm_learn_callback(variable, value):
    print("P: hmm_learn_callback: variable={}, value={}".format(variable, value))
    if USE_WANDB:
        wandb.log({variable: value})


ecoz2.set_random_seed(1)

ecoz2.hmm_learn(N=8,
                sequence_filenames=sequence_filenames,
                hmm_learn_callback=hmm_learn_callback)
