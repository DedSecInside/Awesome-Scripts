#! /bin/bash
#filetypearranger - goes into a specified directory and sorts out the files
####################into folders below that directory for different file types

#check to make sure that only one argument was entered
if [ $# -ne 1 ]
then
	echo "This command requires a single arguement which is a directory"
	echo "USEAGE: filetypearranger.bash [ *directory* ]"
else
	#variable containing the entered direct
	directory=$1
	#check to see if the entered directory is actually a directory
	if [ -d $directory ]
	then
		#these 4 lines makes the dierctories that are need if they are not already created
		mkdir -p $directory/Media
		mkdir -p $directory/Textfiles
		mkdir -p $directory/Documents
		mkdir -p $directory/Other
	else
		echo "ERROR. This directory doesnt exist"
		exit
	fi
	#temp variable to deal with filename that have whitespaces
	createfile=""
	#variable containing all the files in the directory. Cause it list them out
	files=$(ls $directory)
	#loop through each file in the directory
	for filename in $files
	do
		#check to see if the current file is actually a directory
		if [[ ( -d $directory/$filename ) || ( $filename == *".zip"* ) ]]
		then
			echo $filename" is in the same place"
			continue
		#check to see if the current filename is invalid
		#so it treats it as a filename that may have whitespaces
		elif [ ! -f $directory/$filename ]
		then
			#concatenates the current part of the filename with the rest including the whitespaces
			createfile="${createfile}$filename "
			#this variable is used to check if the filename with whitespaces has been made yet
			newfile="${createfile::-1}"
			#check to see if the file with spaces has been made or not so it can decide whether to move on
			if [[ -f $directory/$newfile ]]
			then
				filename=$newfile
				#empties filename builder for the next time it encounters this problem
				createfile=""
			else
				continue
			fi
		fi
		#makes filename executable
		chmod +x $directory/"$filename"
		#this variable get the file type and remove the filename from the string
		filetype=$(file -0 $directory/"$filename" | cut -d $'\0' -f2)
		#check to see if file type is an image or video
		if [[ ($filetype == *"image"* ) || ( $filetype == *"Media"* ) || ( $filetype == *"media"* ) ]]
		then
			#moved the current file into the media folder
			mv $directory/$filename $directory/Media
			echo $filename" has been moved to the media folder"
		#check to see if the file is a text document
		elif [[ $filetype == *"ASCII"* ]]
		then
			#moves the file into the Textfiles folder
			mv $directory/"$filename" $directory/Textfiles
			echo $filename" has been moved to the Textfiles folder"
		#check to see if the file is a word document/PDF
		elif [[ ( $filetype == *"Document"* ) || ( $filetype == *"PDF"* ) || ( $filetype == *"Word"*)]]
		then
			#moves the file into the Documents folder
			mv $directory/"$filename" $directory/Documents
			echo $filename" has been moved to the Documents folder"
		else
			#if the file doesnt meet the other criteria it is moved to the other folder
			mv $directory/"$filename" $directory/Other
			echo $filename" has been moved to the Other folder"
			#user input to see if they want to move there
			read -p "Did you want to move it there. y or n" isMove
			#check to see if the user wanted to move the current file into the other folder
			if [[ "$isMove" == "n" ]]
			then
				#if they didn't it is moved back to the original directory
				mv $directory/Other/"$filename" $dircetory/
				echo $filename" has been moved back to "$directory
			fi
		fi
	done
fi
exit
