#!/usr/bin/env python3
"""
An example program that runs a compiled C++ executable


Some useful links
https://stackoverflow.com/questions/4789837/how-to-terminate-a-python-subprocess-launched-with-shell-true
https://github.com/cython/cython/wiki/tutorials-NumpyPointerToC
https://stackoverflow.com/questions/45133276/passing-c-vector-to-numpy-through-cython-without-copying-and-taking-care-of-me
"""
import sys, subprocess

import numpy as np
from multiply_runner import multiply


def numpy_cython_cpp():
	a = np.arange(12, dtype=np.float64).reshape((3,4))

	print(a)

	multiply(a, 3)

	print(a)

def main():
	print(sys.version)
	print("test")

	# test_no_io()
	# numpy_cython()
	numpy_cython_cpp()

	## Run a process that does not 



if __name__ == '__main__':
    main()