from PIL import Image
from PIL import Image, ImageEnhance

text = Image.open("../assets/text_white.png")
img =Image.open("../assets/evening1.jpg")
text = text.convert("RGBA")
img = img.convert("RGBA")
img = ImageEnhance.Brightness(img).enhance(0.3)
# img.paste(text,(200,200))
# img.show()
# img.save("../output/evening_background2.png")


frontImage = Image.open("../assets/text_white.png")
background = img
# frontImage = frontImage.convert("RGBA")
# background = background.convert("RGBA")
width = (background.width - frontImage.width) // 2
height = (background.height - frontImage.height) // 2
background.paste(frontImage, (width-800, height-800), frontImage)
background.show()
background.save("../output/monji.png", format="png")
