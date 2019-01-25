
Make sure that XCode with command-line tools has been installed and working

Install SUNDIALS -- must be the exact version specified by scikits.odes documentation
https://computation.llnl.gov/projects/sundials/sundials-software
+ Put this in `/usr/local/`
+ Need to manually make some directories
+ I also checked the command-line building instructions included as a PDF with the download

	mkdir build-sundials-2.7.0
	mkdir install-sundials-2.7.0
	cd build-sundials-2.7.0/
	cmake -DLAPACK_ENABLE=ON -DCMAKE_INSTALL_PREFIX=../install-sundials-2.7.0/ ../sundials-2.7.0/
	make install

Now make sure that you have the sundials path properly specified as an environment variable `SUNDIALS_INST`

	export SUNDIALS_INST=$PATH:~/install-sundials-2.7.0

If you mess this up, run `unset $SUNDIALS_INST`

Now install scikits-odes

	pip install scikits.odes


