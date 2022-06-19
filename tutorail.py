from PIL import Image
from PIL import ImageFilter

im = Image.open("wall.png")
# 均值濾波
im1 = im.filter(ImageFilter.BLUR)
# 找輪廓
im2 = im.filter(ImageFilter.CONTOUR)
# 邊緣檢測
im3 = im.filter(ImageFilter.FIND_EDGES)
im.show()
im1.show()
im2.show()
im3.show()