from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ecoz2_extension = Extension(
    name="ecoz2py",
    sources=["ecoz2.pyx"],
    libraries=["ecoz"],
    include_dirs=["../ecoz2/src/include"],
    library_dirs=[
      "../ecoz2/_out/lib",
    ],
)
setup(
    name="ecoz2py",
    ext_modules=cythonize([ecoz2_extension])
)
