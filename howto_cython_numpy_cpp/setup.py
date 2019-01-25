#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy

ext_modules = [Extension(
	"multiply_runner",
	["multiply_runner.pyx", "multiply.cpp"],
	language="c++",
	extra_compile_args=["-std=c++11"],
    extra_link_args=["-std=c++11"]
	)]
# ext_modules = [Extension("multiply",
#                              sources=["multiply_cpp.pyx", "cpp_multiply.cpp"],
#                              include_dirs=[numpy.get_include()])]

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules,
    include_dirs=[numpy.get_include()]
)

# from distutils.core import setup

# from Cython.Build import cythonize

# setup(ext_modules=cythonize("multiply_cpp.pyx"))