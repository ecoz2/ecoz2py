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
    
    # on linux  (build ok on a centos7 docker container)
    $ make
    
    $ cd ..
    
A more regular test as "client" of the lib:

    $ export PYTHONPATH=.:ecoz2py
    
    $ python ecoz2_hmm_learn_test.py
    USE_WANDB: False
    ECOZ2 C version: b'0.3.0'
    ecoz2_set_random_seed: seed=1
    hmm_learn: num_sequences = 11
      0: ecoz2py/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__10079.092_10080.35.seq
      1: ecoz2py/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__680.14154_680.8046.seq
      2: ecoz2py/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__1089.723_1090.6355.seq
      3: ecoz2py/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__5067.5444_5070.2764.seq
      4: ecoz2py/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__12907.783_12909.293.seq
      5: ecoz2py/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__588.77454_591.3191.seq
      6: ecoz2py/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__15415.037_15417.307.seq
      7: ecoz2py/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__1068.8552_1069.205.seq
      8: ecoz2py/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__2926.575_2929.6223.seq
      9: ecoz2py/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__10540.822_10543.197.seq
     10: ecoz2py/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__7145.495_7147.0107.seq
    
    N=8 M=1024 type=3  #sequences = 11  max_T=201
    val_auto = 0.3   log=-1.20397
    max_iterations= -1
    . 1: Δ = +43.4016  sum_log_prob = -5228.75 sum_log_prob_prev = -5272.16  'B'  (0.012s)
    P: hmm_learn_callback: variable=sum_log_prob, value=-5228.7540730621
    . 2: Δ = +14.7201  sum_log_prob = -5214.03 sum_log_prob_prev = -5228.75  'B'  (0.010s)
    P: hmm_learn_callback: variable=sum_log_prob, value=-5214.033997162085
    . 3: Δ = +7.04086  sum_log_prob = -5206.99 sum_log_prob_prev = -5214.03  'B'  (0.011s)
    P: hmm_learn_callback: variable=sum_log_prob, value=-5206.993136338338
    . 4: Δ = +20.8825  sum_log_prob = -5186.11 sum_log_prob_prev = -5206.99  'B'  (0.010s)
    P: hmm_learn_callback: variable=sum_log_prob, value=-5186.110655885082
    . 5: Δ = +36.1808  sum_log_prob = -5149.93 sum_log_prob_prev = -5186.11  'B'  (0.012s)
    P: hmm_learn_callback: variable=sum_log_prob, value=-5149.9298841011805
    . 6: Δ = +48.584  sum_log_prob = -5101.35 sum_log_prob_prev = -5149.93  'B'  (0.010s)
    P: hmm_learn_callback: variable=sum_log_prob, value=-5101.345860730357
    . 7: Δ = +258.061  sum_log_prob = -4843.29 sum_log_prob_prev = -5101.35  'B'  (0.010s)
    P: hmm_learn_callback: variable=sum_log_prob, value=-4843.285099164055
    . 8: Δ = +0.660446  sum_log_prob = -4842.62 sum_log_prob_prev = -4843.29  'B'  (0.010s)
    P: hmm_learn_callback: variable=sum_log_prob, value=-4842.624653418044
    
    
        Model: data/hmms/N8__M1024_t3__a0.3/B.hmm   className: 'B'
        N=8 M=1024 type: cascade-3
        restriction: 1e-05
                #sequences: 11
                auto value: 0.3
              #refinements: 8
                  Σ log(P): -4.842625e+03
    training took 0.10s
    
----

Note: `ecoz2_vq_learn_test.py` also runs fine, but requires some data from the `ecoz2-whale` project.
