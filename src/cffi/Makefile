
ecoz2py: _ecoz2_extension.so


_ecoz2_extension.so: ecoz2_extension_build.py *.c *.h
	python ecoz2_extension_build.py
	mv _ecoz2_extension.cpython-38-darwin.so _ecoz2_extension.so

test: ecoz2py
	python ecoz2_extension_test.py
