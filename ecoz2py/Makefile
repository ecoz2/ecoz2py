all: test

_ecoz2_extension.so: ecoz2_extension_build.py ecoz2_extension.h
	C_INCLUDE_PATH=../ecoz2/src/include python ecoz2_extension_build.py
	mv _ecoz2_extension.cpython-38-darwin.so _ecoz2_extension.so

test: _ecoz2_extension.so
	python ecoz2_extension_test.py

clean:
	rm *.so *.o _ecoz2_extension.c
