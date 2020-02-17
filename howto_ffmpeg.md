Various commands and shortcuts for working with ffmpeg

### Turn folder of frames into a video

	ffmpeg -r 20 -i pic%03d.png -vcodec libx264 -pix_fmt yuv420p -crf 25 my_video.mov

`-r` specifies the frame rate
`%03d` says that the images have three digits
`\crf` sets video quality (lower number is higher quality)

To invert the colors of each image (or apply any other image filter), add `-filter negate` anywhere before the output video name

### Watermark a video

Follow [the instructions here](http://ksloan.net/watermarking-videos-from-the-command-line-using-ffmpeg-filters/)

	ffmpeg -i input.mov -i watermark_small.png -filter_complex "overlay=(.7*main_w):(.94*main_h)" output.mov

Places watermark in bottom right corner


### Extract audio from video

For an MP4 file this is easy

	ffmpeg -i input.mp4 output.mp3


### Encode a video for Twitter

Use FFMPEG, for mp4 the file shape has to be even in both dimensions; can omit the -filter crop below if this is already true

	ffmpeg -i video2_small.mp4 -filter:v "crop=3008:3000:0:0" -vcodec libx264 -acodec aac output.mp4


### Deshake a video

	ffmpeg -i input.mp4 -vf deshake="rx=64:ry=64"  -an output.mov

The flags `-rx`  and `-ry` are optional flags taken from this list [here](https://ffmpeg.org/ffmpeg-filters.html#deshake)

### Convert a directory of FLAC to ALAC for iTunes

Using ffmpeg

	for i in *.flac ; do
	    ffmpeg -i "$i" -acodec alac "$(basename "${i/.flac}").m4a"
	    sleep 2
	    # may need to adjust sleep time for processor speed                               
	done

I saved this as a bash script, so just cd into the directory containing the FLAC files and then run

	bash ~/codebits/utility_scripts/flac2alac.sh

### Merge three videos in xy as a mosiac using FFMPEG

The height and widht parameters have to be calculated very carefully---any extra space will be filled with black thanks to the "color" option below

Crop mosaic length to the shortest video length

	ffmpeg -i 1.mov -i 2.mov -i 3.mov -filter_complex "color=s=4912x1502:c=black [base];[0:v] setpts=PTS-STARTPTS, scale=1504x1502 [left];[1:v] setpts=PTS-STARTPTS, scale=1504x1502 [middle];[2:v] setpts=PTS-STARTPTS, scale=1504x1502 [right];[base][left] overlay=shortest=1 [tmp1];[tmp1][middle] overlay=shortest=1:x=1704 [tmp2];[tmp2][right] overlay=shortest=1:x=3408" -c:v libx264 output_merge.mov

Remove the `shortest` flag to set the mosaic length to length of longest video (pad with ending frames of other videos)
1520x1507

	ffmpeg -i inv1.mov -i inv3.mov -filter_complex "color=s=3340x1508:c=black [base];[0:v] setpts=PTS-STARTPTS, scale=1520x1508 [left];[1:v] setpts=PTS-STARTPTS, scale=1520x1508 [right];[base][left] overlay=shortest=1 [tmp1];[tmp1][right] overlay=shortest=1:x=1820" -c:v libx264 output_merge2.mov



Note that this throws an error if the video heights or widths are not even numbers of pixels


[Source 1](https://stackoverflow.com/questions/33330279/ffmpeg-selects-shortest-movie-but-leaves-full-length-audio)[Source 2](
https://trac.ffmpeg.org/wiki/Create%20a%20mosaic%20out%20of%20several%20input%20videos)
