all: ecoz2py

lib:
	cd ../ecoz2 && make lib

ecoz2py: setup.py ecoz2.pyx lib
	python setup.py build_ext --inplace && rm -f ecoz2.c && rm -Rf build
	python -c 'import ecoz2py; print(ecoz2py.version())'
	python -c 'import ecoz2py; print(ecoz2py.foo(b"baz"))'

clean:
	rm *.so
