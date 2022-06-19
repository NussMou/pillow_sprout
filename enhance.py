from PIL import Image, ImageEnhance

text = Image.open("text.png")
img =Image.open("evening1.jpg")
text = text.convert("RGBA")
img = img.convert("RGBA")
img = ImageEnhance.Brightness(img).enhance(0.3)
# img.paste(text,(200,200))
# img.show()
img.save("assets/evening_background2.png")

# # Calculate width to be at the center
# width = (background.width - frontImage.width) // 2

# # Calculate height to be at the center
# height = (background.height - frontImage.height) // 2

# # Paste the frontImage at (width, height)
# background.paste(frontImage, (width, height), frontImage)

# # Save this image
# background.save("new.png", format="png")
