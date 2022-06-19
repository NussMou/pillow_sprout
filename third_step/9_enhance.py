from PIL import Image, ImageEnhance

text = Image.open("../assets/text_white.png")
img =Image.open("../assets/evening1.jpg")
text = text.convert("RGBA")
img = img.convert("RGBA")
img = ImageEnhance.Brightness(img).enhance(0.3)
# img.paste(text,(200,200))
img.show()
img.save("../output/evening_background2.png")

