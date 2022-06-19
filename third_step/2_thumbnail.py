from PIL import Image

img = Image.open("../assets/stone.png")
print(img.size)
img.show()

img.thumbnail((256, 256))
print(img.size)
img.show()
img.save("../output/thumbnail.png")
