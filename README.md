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

#### cffi

    cd cffi    
    make

#### cython

    cd cython    
    make
