from PIL import Image

img = Image.open("../assets/stone.png")
img = img.rotate(45)
print(img.size)
left = 100
top = 100
right = 1000
bottom = 1000
img = img.crop((left,top,right,bottom))
img.show()