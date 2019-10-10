# Author: Deepak Chauhan
# Github: https://github.com/RoyalEagle73

import os
count = 0

## CODE TO CHECK AND PRINT FOR FILES HAVING LOWER CASE STARTING
for x,y,z in os.walk("Folder Location Here"):
	root = str(x)
	for i in z:
		if i[0].islower():
			count += 1


if count!=0:

	print("%d files available for change"%(count))

	response = input("Enter Y/N if want to continue to capitalize all of them :")

	if response=='Y' or response=='y':
		count = 0

		# CODE TO CHANGE THE FILES
		for x,y,z in os.walk("Folder Location Here"):
			root = str(x)
			for i in z:
				if i[0].islower():
					first_letter = i[0].upper()
					final_command = "mv " + root+"/"+i +" "+(root+"/"+first_letter+i[1:])
					count += 1
					os.popen(final_command)
		print(str(count) + " files changed\n\nThanks for using the tool :)")
	else:
		print("Thanks for using the tool :)")

else:
	print("No files available for change.\nThanks for using the tool :)")
