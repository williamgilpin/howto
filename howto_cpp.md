### Installing an editor / build system

I am using OSX. I started out with Sublime Text. I first made sure that XCode had command line tools installed.

Pick a Build System using Command + Shift + B. This has two options: just build, or build+run. Depending on the dependencies. it might make sense to build only
+ However, for basic scripts I just Build+Run [Super + B], for which Sublime will give Terminal output
+ To run without re-building, select "Build only" as the build system, then build only with Super+B. Then run only using

Adding modules appears to consist of just including the files on the path in a header file, similar to MATLAB
+ The MAKEFILE can include a path to an external library, if needed



## Resources


Here is a nice thread on the basics of installing C++ packages and using make on OSX. See [here](https://www.boost.org/doc/libs/1_69_0/more/getting_started/unix-variants.html)
+ Standard place to install libraries is `/usr/local/` and the header files go in `/usr/local/include`
+ However, it might be good to install somewhere else and just re-link, since it's good to avoid polluting system folders with 3rd party stuff

Some very nice [slides with the basics of C and C++](http://vergil.chemistry.gatech.edu/resources/programming/programming.pdf)


### Nice demonstrations of simple physical problems in Boos

[Here](https://github.com/headmyshoulder/odeint-v2/tree/master/examples) and more specifically[here](https://github.com/headmyshoulder/odeint-v2/blob/master/examples/phase_oscillator_ensemble.cpp)


### A Transition Guide: Python to C++
Goldwasser, Letscher
https://pdfs.semanticscholar.org/9ad1/030685050e949d1a3d6d92bababcbe075e07.pdf

+ Guide for learning C++ starting from Python


### CS106x at Stanford
https://web.stanford.edu/class/archive/cs/cs106x/cs106x.1182/lectures/10-23/13-pointer-struct.pdf

Need SUID to access old lecture notes
+ Uses a non-standard library for a lot of data structures, mainly for pedagogical purposes (simpler API). but this makes the slides harder to use as a reference (in my experience)

## Installing Boost

Can just do this with Homebrew

	brew install Boost

There are also detailed instructions from the official documentation [here](https://www.boost.org/doc/libs/1_69_0/more/getting_started/unix-variants.html).

Brew puts the boost library under `/usr/local/Cellar/boost/1.68.0_1` instead of the official instructions, which put it under `/usr/local/boost/1.68.0_1`



## Some notes on learning C++


C++ has three variable types: pointers, values, and references

Pointers take up their own memory address; can be used to put things in and out of that address
Pointers are more general than a reference because they can point to `NULL`
Pointers can be reassigned:

Pointer example

int x = 5;
int y = 6;
int *p;
p =  &x;
p = &y;


Reference example

int x = 5;
int y = 6;
int &r = x;


From https://www.geeksforgeeks.org/pointers-vs-references-cpp/