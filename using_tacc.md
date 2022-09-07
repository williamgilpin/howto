
Useful information

+ TACC getting started [guide](https://wikis.utexas.edu/display/CoreNGSTools/Getting+started+at+TACC)
+ TACC conda and advanced [guide](https://wikis.utexas.edu/display/bioiteam/Linux+and+stampede2+Setup+--+GVA2021#Linuxandstampede2SetupGVA2021-MovingbeyondthepreinstalledcommandsonTACC)
+ Run Jupyter in browser via [TACC Vis portal](https://vis.tacc.utexas.edu/).
+ Notes on getting started with Python and conda [here](https://www.wgilpin.com/cphy/labs/getting_started_with_python.html)

# Using conda on Lonestar

Since conda is not installed by default, you cannot currently use `module load conda` as you would on Stampede

In your user folder, make a directory called `src` and then use wget to download the Miniconda 64 bit Linux installer into the folder (go to the Miniconda page, find the first Linux installer, and right click to copy the link address). Follow the Miniconda instructions to run the installer bash script.

Add your conda install to your path

    export PATH="~/miniconda/bin:$PATH"

test that everything is working

    conda list --envs

You can activate, install packages, etc as you would for a local conda environment


# Using Jupyter notebooks on TACC

In a web browser, visit the [TACC Vis portal](https://vis.tacc.utexas.edu/).

Create a job with your desired resources and partition. Leave the "reservation" field blank.