from PIL import Image, ImageEnhance
img =Image.open("evening1.jpg")
img = ImageEnhance.Color(img).enhance(0.1)
img.show()
img.save("assets/evening_background")