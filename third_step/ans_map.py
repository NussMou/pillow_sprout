from PIL import Image
from PIL import ImageFilter

img = Image.open("../assets/wall.png")

img1 = img.filter(ImageFilter.CONTOUR)

img2 = img.filter(ImageFilter.EMBOSS)
img.show()
img1.show()
img2.show()