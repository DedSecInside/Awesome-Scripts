import PIL
import os
import os.path
from PIL import Image

# Replace "image directory" with the path of the folder with your images in
img_dir = r'Image directory'

print('Bulk images resizing started...')

for img in os.listdir(img_dir):
	f_img = img_dir + img
	f, e = os.path.splitext(img_dir + img)
	img = Image.open(f_img)
	# Replace "80", "160" with the sizes you want.
	img = img.resize((80, 160))
	# This gives the resized images it's name which is currently its old name with _resized at the end.
	img.save(f + '_resized.jpg')

print('Bulk images resizing finished...')