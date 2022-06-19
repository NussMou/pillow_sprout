from PIL import Image

frontImage = Image.open("../assets/text_white.png")
background = Image.open("../assets/evening_background2.png")
# frontImage = frontImage.convert("RGBA")
# background = background.convert("RGBA")
width = (background.width - frontImage.width) // 2
height = (background.height - frontImage.height) // 2
background.paste(frontImage, (width-800, height-800), frontImage)
background.show()
background.save("../output/monji.png", format="png")
