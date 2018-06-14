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

	>awk '{print $1" "$2" "$3" "$4}' lol.txt > lol2.txt

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

Can drop the part in quotes in the first line if you just want to rename without selecting any data

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

# Format videos for Twitter

Use FFMPEG, for mp4 the file shape has to be even in both dimensions; can omit the -filter crop below if this is already true

	ffmpeg -i video2_small.mp4 -filter:v "crop=3008:3000:0:0" -vcodec libx264 -acodec aac output.mp4

