import os

print "Choose an option - "
print "1. N largest files. "
print "2. N smallest files. "
print "3. N most recently used files. "
print "4. N least recently used files. "

option = input("Your option?\n")
directory = raw_input("Absolute path of directory\n")
N = input("Number of files you want to list?\n")

files = os.listdir(directory)

def list_N_files(all_files):
    """
    Lists all files

    Args:
        all_files: (str): write your description
    """
	print "\n".join(all_files[:N])

if option==1:
	sorted_file_list = sorted(files, key=lambda x: os.stat(os.path.join(directory, x)).st_size, reverse=True)
	list_N_files(sorted_file_list)

elif option == 2:
	sorted_file_list = sorted(files, key=lambda x: os.stat(os.path.join(directory, x)).st_size )
	list_N_files(sorted_file_list)

elif option == 3:
	sorted_file_list = sorted(files, key=lambda x: os.stat(os.path.join(directory, x)).st_mtime, reverse=True)
	list_N_files(sorted_file_list)

elif option == 4:
	sorted_file_list = sorted(files, key=lambda x: os.stat(os.path.join(directory, x)).st_mtime)
	list_N_files(sorted_file_list)
	
else:
	print("Invalid option")