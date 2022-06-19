from PIL import Image
img = Image.open("../assets/brown.png")

# RGB_tuple = img.getpixel((w, h))  待會和putpixel一起看
# print("RGB : " + RGB_tuple)

print("size =" , img.size)
print("image_format =",img.format)
print("mode =",img.mode)

img.show()
img.save("../output/beginning.png")
