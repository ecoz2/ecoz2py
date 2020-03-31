from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ecoz2_extension = Extension(
    name="ecoz2py",
    sources=["src/ecoz2.pyx"],
    libraries=["ecoz"],
    library_dirs=["ecoz2/_out/lib"],
    include_dirs=["ecoz2/src/include"]
)
setup(
    name="ecoz2py",
    ext_modules=cythonize([ecoz2_extension])
)
