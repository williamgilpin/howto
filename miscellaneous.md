Various small tricks I've found helpful. Most of these only work on OSX or Linux.

# Speed up a time machine backup

This removes the CPU use throttling, so only use it when you aren't actively using the computer

	sudo sysctl debug.lowpri_throttle_enabled=0

Once the backup is complete

	sudo sysctl debug.lowpri_throttle_enabled=1

# Watermark a video with FFMPEG

Follow [the instructions here](http://ksloan.net/watermarking-videos-from-the-command-line-using-ffmpeg-filters/)

	ffmpeg -i input.mov -i watermark_small.png -filter_complex "overlay=(.7*main_w):(.94*main_h)" output.mov

Places watermark in bottom right corner


# Extract audio from video using FFMPEG

For an MP4 file this is easy

	ffmpeg -i input.mp4 output.mp3

# Remove columns from a space delimited txt file

Keep only the first four columns from the file `lol.txt`

	> awk '{print $1" "$2" "$3" "$4}' lol.txt > lol2.txt

Run this as a script for all of the files in a directory

	for file in *.txt
	do
	    awk '{print $1" "$2" "$3" "$4}' $file > $file\_edited.txt
	    echo $file
	done

Note that we had to use the system-specific escape character "\_" in order to clear the underscore, this could be different on different platforms

To rename files with sequential numbers, run a similar script:

	a=1
	for file in *.txt
	do
	    awk '{print $1" "$2" "$3" "$4}' $file > $velocity$a.txt
	    let a=a+1
	    echo $file
	done

Can 

# Sublime Text customization of settings

Open preferences from the menus and put your preferences in a single pair of curly braces (XML formatting)

	{
		"color_scheme": "Packages/User/Tomorrow-Night.tmTheme",
		"font_size": 11,
		"open_files_in_new_window": false,
		"ignored_packages":
		[
			"Vintage"
		]
	}

# Put parentheses around all citations in LaTeX

This is useful for switching a document over to NatBib

	\renewcommand{\cite}[1]{(\citenum{#1})} % parentheses around citations

This can go anywhere in the preamble

# Run multiple Mathematica notebooks at once

The goal here is to have two notebooks open that don't interact with eachother---separate kernels and namespaces

`Evaluation > Kernel Configuration`

Add a new kernel with a cool name, set "Launch on" to "Local Machine"

Open new notebook, go to `Evaluation > Notebook's Kernel >` Select the cool kernel name you just made

[See this article](http://support.wolfram.com/kb/12425)

# Shrink PDF files with minimal loss of quality

Install ghostscript if you don't have it

	brew install ghostscript

Compress the PDF file using the command

	gs -sDEVICE=pdfwrite -dNOPAUSE -dQUIET -dBATCH -dPDFSETTINGS=/default -dCompatibilityLevel=1.4 -sOutputFile=output.pdf input.pdf

For different quality, try these flags:

Use the following ghostscript command:

	-dPDFSETTINGS=/screen lower quality, smaller size.
	-dPDFSETTINGS=/ebook for better quality, but slightly larger pdfs.
	-dPDFSETTINGS=/prepress output similar to Acrobat Distiller "Prepress Optimized" setting
	-dPDFSETTINGS=/printer selects output similar to the Acrobat Distiller "Print Optimized" setting
	-dPDFSETTINGS=/default selects output intended to be useful across a wide variety of uses, possibly at the expense of a larger output file

More information on [StackExchange](https://askubuntu.com/questions/113544/how-can-i-reduce-the-file-size-of-a-scanned-pdf-file)

# Open tar gz file

# Format videos for Twitter

Use FFMPEG, for mp4 the file shape has to be even in both dimensions; can omit the -filter crop below if this is already true

	ffmpeg -i video2_small.mp4 -filter:v "crop=3008:3000:0:0" -vcodec libx264 -acodec aac output.mp4


# Deshake a video

	ffmpeg -i input.mp4 -vf deshake="rx=64:ry=64"  -an output.mov

The flags `-rx`  and `-ry` are optional flags taken from this list [here](https://ffmpeg.org/ffmpeg-filters.html#deshake)

# Convert a directory of FLAC to ALAC for iTunes

Using ffmpeg

	for i in *.flac ; do
	    ffmpeg -i "$i" -acodec alac "$(basename "${i/.flac}").m4a"
	    sleep 2
	    # may need to adjust sleep time for processor speed                               
	done

I saved this as a bash script, so just cd into the directory containing the FLAC files and then run

	bash ~/codebits/utility_scripts/flac2alac.sh

# Make spectrograms to check quality of audio files

Using sox

	sox audiofile.flac -n spectrogram

A good FLAC file should have features at 22 kHz. A transcode low quality will have a plateau around 19 kHz (with some spikes). Great info [here](https://dsp.stackexchange.com/questions/20563/how-to-know-if-a-audio-file-is-real-lossless-using-its-spectrogram)


# Update packages in MacTeX

There is an actual package manager called `tlmgr` installed by default on TeX Live and MacTeX

First, update it

	tlmgr update --self

Can install a package like this

	tlmgr install revtex

Can view all installed packages like this

	tlmgr update --list

Can update everything with this

	tlmgr update --all

Note: I had to sudo all of these, since I installed MacTeX like a standard application on macOS


# Fix focusing issue on Sublime text OSX

Add the following plugin "Tools > Developer > New Plugin" and save with a descriptive name.
Copied from [this GitHub thread](https://github.com/SublimeTextIssues/Core/issues/448)

	import sublime
	import sublime_plugin
	import os

	cmd = '''
	tell application \\"System Events\\"
	    tell application process \\"Sublime Text\\"
	        set frontmost to true
	    end tell
	end tell
	'''

	class FocusOnLoad (sublime_plugin.EventListener):
	    def on_load(self, view):
	        os.system('osascript -e "{0}"'.format(cmd))


# Extract data from tables in a PDF file

Use this software [here](https://tabula.technology/)
+ Install the software and run it in order to start the server
+ Then, navigate to the server in your browser in order to use the software (instructions are in the README)


# Merge three videos in xy as a mosiac using FFMPEG

The height and widht parameters have to be calculated very carefully---any extra space will be filled with black thanks to the "color" option below

Crop mosaic length to the shortest video length

	ffmpeg -i 1.mov -i 2.mov -i 3.mov -filter_complex "color=s=4912x1502:c=black [base];[0:v] setpts=PTS-STARTPTS, scale=1504x1502 [left];[1:v] setpts=PTS-STARTPTS, scale=1504x1502 [middle];[2:v] setpts=PTS-STARTPTS, scale=1504x1502 [right];[base][left] overlay=shortest=1 [tmp1];[tmp1][middle] overlay=shortest=1:x=1704 [tmp2];[tmp2][right] overlay=shortest=1:x=3408" -c:v libx264 output_merge.mov

Remove the `shortest` flag to set the mosaic length to length of longest video (pad with ending frames of other videos)
1520x1507

	ffmpeg -i inv1.mov -i inv3.mov -filter_complex "color=s=3340x1508:c=black [base];[0:v] setpts=PTS-STARTPTS, scale=1520x1508 [left];[1:v] setpts=PTS-STARTPTS, scale=1520x1508 [right];[base][left] overlay=shortest=1 [tmp1];[tmp1][right] overlay=shortest=1:x=1820" -c:v libx264 output_merge2.mov



Note that this throws an error if the video heights or widths are not even numbers of pixels


Sources


https://stackoverflow.com/questions/33330279/ffmpeg-selects-shortest-movie-but-leaves-full-length-audio
https://trac.ffmpeg.org/wiki/Create%20a%20mosaic%20out%20of%20several%20input%20videos