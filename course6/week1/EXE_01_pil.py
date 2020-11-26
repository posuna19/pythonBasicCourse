import PIL

print("Hello")

import sys;
print('Python %s on %s' % (sys.version, sys.platform))
#sys.path.extend([WORKING_DIR_AND_PYTHON_PATHS])


from PIL import Image
im = Image.open("EXE_01_pil_image.JPG")
im.rotate(90).show()

help(PIL)

#from PIL import Image
im = Image.open("EXE_01_pil_image.JPG")
new_im = im.resize((640,480))
new_im.save("example_resized.jpg")

#from PIL import Image
im = Image.open("EXE_01_pil_image.JPG")
new_im = im.rotate(90)
new_im.save("example_rotated.jpg")

im = Image.open("EXE_01_pil_image.JPG")
im.rotate(180).resize((640, 180)).save("flipped_resized_example.jpg")
