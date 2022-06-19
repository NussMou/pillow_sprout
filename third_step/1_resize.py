from PIL import Image

img = Image.open("../assets/brown.png")
(w, h) = img.size
print(w, h)
img.show()

new = img.resize((256, 512))
(w,h) = new.size
print(w,h)
new.show()
new.save("../output/resize_save.png")
