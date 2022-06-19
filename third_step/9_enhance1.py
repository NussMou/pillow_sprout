from PIL import Image, ImageEnhance
img =Image.open("../assets/evening1.jpg")
img = ImageEnhance.Color(img).enhance(0.1)
img.show()
img.save("../output/evening_background.png")