all: ecoz2py

lib:
	cd ecoz2 && make lib

ecoz2py: src/cython/setup.py src/cython/ecoz2.pyx lib
	python src/setup.py build_ext --inplace && rm -f src/ecoz2.c && rm -Rf build
	python -c 'import ecoz2py; print(ecoz2py.version())'
	python -c 'import ecoz2py; print(ecoz2py.foo(b"baz"))'
