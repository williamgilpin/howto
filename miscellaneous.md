Various small tricks I've found helpful. Most of these only work on OSX or Linux.

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
