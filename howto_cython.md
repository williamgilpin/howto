


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


### Runnin a C/C++ executable with Numpy arrays and Cython

Personally, I found it easier to use Cython with standalone .pyx files, rather than trying to build cells within a Jupyter notebook. One nice thing about using Cython for this is that it can avoid copying the array, and instead it directs the executable directly to the memory locations of the array.
The approach below is a condensed version of [this tutorial](https://github.com/cython/cython/wiki/tutorials-NumpyPointerToC)

Your project structure needs to look like this:

	integrator_project/
	├── integrator.cpp
	├── run_integrator.pyx
	├── setup.py
	└── my_script.py

+ Enter a venv with Python 3 and Cython installed and working
+ First, compile `integrator.cpp`. 
+ Make a `run_integrator.pyx` file to deal with input/output from the numpy array. Here is a minimal example

	import cython

	# import both numpy and the Cython declarations for numpy
	import numpy as np
	cimport numpy as np

	# declare the interface to the C code
	cdef extern void integrator (double* array, double value, int m, int n)

	@cython.boundscheck(False)
	@cython.wraparound(False)
	def run_integrator(np.ndarray[double, ndim=2, mode="c"] input not None, double value):
	    
	    cdef int m, n
	    m, n = input.shape[0], input.shape[1]

	    integrator (&input[0,0], value, m, n)

	    return None

+ Now, make a `setup.py` file to help organize the build process

	#!/usr/bin/env python

	from distutils.core import setup
	from distutils.extension import Extension
	from Cython.Distutils import build_ext

	import numpy

	setup(
	    cmdclass = {'build_ext': build_ext},
	    ext_modules = [Extension("run_integrator",
	                             sources=["run_integrator.pyx", "integrator.cpp"],
	                             include_dirs=[numpy.get_include()])],
	)


+ Now, compile the .pyx file using `python setup.py build_ext --inplace`
+ Now you are ready to use the function. In your python script `my_script.py` add an import statement `import run_integrator` and use run_integrator as a normal function