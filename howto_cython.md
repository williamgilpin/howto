


### Running a C/C++ executable from within Python, without any IO

Compile your executable, and then use the subprocess library. Then, in your Python script, use some variant of this:

	def test_no_io():
		'''
		Run a process that takes no input and produces no output
		'''
		## Shell=False helps the process terminate
		process = subprocess.Popen("./hello", shell=False)
		
		## Get exit codes
		out, err = process.communicate()
		errcode = process.returncode
		print(errcode)

		process.kill() 
		process.terminate()

This will run the executable `hello`, and it will dump any prints to the command line. A lot of the fancy syntax here is just to ensure that the process gets killed off


### Running a C/C++ executable with Numpy arrays and Cython

See examples in the "cython_numpy_cpp/"  subdirectory

Personally, I found it easier to use Cython with standalone .pyx files, rather than trying to build cells within a Jupyter notebook. One nice thing about using Cython for this is that it can avoid copying the array, and instead it directs the executable directly to the memory locations of the array.
The approach below is a condensed version of [this tutorial](https://github.com/cython/cython/wiki/tutorials-NumpyPointerToC) modified for C++ using [these instructions](https://stackoverflow.com/questions/45133276/passing-c-vector-to-numpy-through-cython-without-copying-and-taking-care-of-me)

Your project structure needs to look like this:

	integrator_project/
	├── multiply.h
	├── multiply.cpp
	├── multiply_runner.pyx
	├── setup.py
	└── my_script.py

+ Enter a venv with Python 3 and Cython installed and working
+ First, compile `multiply.cpp`, which is a file containing the function`cpp_multiply`
+ Make a `multiply_runner.pyx` file to deal with input/output from the numpy array. Here is a minimal example

	import cython

	# import both numpy and the Cython declarations for numpy
	import numpy as np
	cimport numpy as np
	np.import_array()

	# declare the interface to the C code
	cdef extern from "multiply.h":
	    void cpp_multiply (double* array, double multiplier, int m, int n)

	@cython.boundscheck(False)
	@cython.wraparound(False)
	def multiply(np.ndarray[double, ndim=2, mode="c"] input not None, double value):
	    
	    cdef int m, n

	    m, n = input.shape[0], input.shape[1]

	    cpp_multiply (&input[0,0], value, m, n)

	    return None

+ Now, make a `setup.py` file to help organize the build process

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

	setup(
	    cmdclass = {'build_ext': build_ext},
	    ext_modules = ext_modules,
	    include_dirs=[numpy.get_include()]
	)


+ Now, compile the .pyx file using `python setup.py build_ext --inplace`
+ Now you are ready to use the function. In your python script `my_script.py` add an import statement `from multiply_runner import multiply` and use multiply as a normal function. The name of the function is its name in the .pyx file, regardless of its name in the original cpp and h files


## Optimizing Cython code

You can see when Python is getting instead of C called by running

	cython -a oscillator_funcs.pyx

And viewing the resulting HTML file.

Good tips on optimizing Cython code in the document [Using Cython to Speed up Numerical Python Programs](https://www.simula.no/file/simulasc578pdf/download)

