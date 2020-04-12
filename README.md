# ecoz2 python wrapper

**WIP**

## Development

### Setup

    virtualenv -p python3 .env
    source .env/bin/activate
    pip install -r requirements.txt

### Build

[ecoz2](https://github.com/ecoz2/ecoz2) is included as a submodule.

    git submodule foreach "(git checkout master; git pull)"

#### cffi based wrapper

    $ (cd ecoz2py && make)
    
    $ export PYTHONPATH=.:ecoz2py
    $ python ecoz2_hmm_learn_test.py
    VERSION: b'The ecoz2 version'
    # ../ecoz2-whale/exerc01/data/predictors/TRAIN/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__10079.092_10080.35.prd:
    # className='B', T=81, P=36
    r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,r20,r21,r22,r23,r24,r25,r26,r27,r28,r29,r30,r31,r32,r33,r34,r35,r36
    ...
    
    
#### cython

Some initial attempts with Cython

    cd cython    
    make
