# python bindings for ecoz2

WIP

## Development

### Setup

    virtualenv -p python3 .env
    source .env/bin/activate
    pip install -r requirements.txt

### Build

[ecoz2](https://github.com/ecoz2/ecoz2) is included as a submodule,
with selected functionality exposed via
https://cython.readthedocs.io/.


    git submodule foreach "(git checkout master; git pull)"
    
    make
