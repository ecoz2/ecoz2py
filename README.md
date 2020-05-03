# ecoz2 python wrapper

**WIP**

## Development

### Setup

    pip3 install [--user] virtualenv
    
    virtualenv -p python3 .env
    source .env/bin/activate    
    pip install -r requirements.txt

### Build

[ecoz2](https://github.com/ecoz2/ecoz2) is included as a submodule.

    git submodule foreach "(git checkout master; git pull)"

#### cffi based wrapper

    $ cd ecoz2py
    
    # on a mac with gcc (not clang):
    $ CC=gcc-9 make
    
    # on linux
    $ make
    
    $ cd ..
    
A more regular test as "client" of the lib:

    $ export PYTHONPATH=.:ecoz2py
    
    $ python ecoz2_hmm_learn_test.py
    USE_WANDB: False
    ECOZ2 C version: b'0.3.0'
    ecoz2_set_random_seed: seed=1
    hmm_learn: num_sequences = 410
    ...
    409: ../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/A/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__8674.046_8675.54.seq

    N=8 M=1024 type=3  #sequences = 410  max_T=179
    val_auto = 0.3   log=-1.20397
    max_iterations= -1
    . 1: Δ = +1347.08  sum_log_prob = -222208 sum_log_prob_prev = -223555  'A'  (0.313s)
    ...
    
