from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

# Declare some global variables to use
img_list = []
page = None
root = Tk()
root.title('Opening files')

r = 1
c = '3'


def open_file():
    """
    Opens a list in a list.

    Args:
    """
    # Open images with GUI

	global page
	global img_list
	global r
	global c
	root.filename = filedialog.askopenfilenames(initialdir="images/",
												title="Select a file",
												filetypes=(("All files", "*.*"),))

	file_list = list(root.filename)
	for name in file_list:
		page = Image.open(name)
		page = page.convert("RGB")
		img_list.append(page)
		my_label = Label(text=name, anchor='w').grid(row=r, column=str(c))
		r += 1


def generate_pdf():
    """
    Generate a pdf

    Args:
    """
    # Generate PDF

	global page
	global img_list
	page = img_list[0]
	page.save(r' '+ str(e.get()) + '.pdf', save_all=True, append_images=img_list[1:])


# Initialize Button widgets for tkinter
add_file_button = Button(root, text="Add file", command=open_file, width=15)
generate_button = Button(root, text="Generate PDF", command=generate_pdf, width=15)
file_name = Label(root, text="Enter your file name: ")
e = Entry(root)


# Align Buttons
add_file_button.grid(row=1, column='1')
generate_button.grid(row=2, column='1')
file_name.grid(row=3, column='1')
e.grid(row=3, column='2')


if __name__ == "__main__":
    root.mainloop()