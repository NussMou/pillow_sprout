from PIL import Image, ImageDraw, ImageFilter
img = Image.new("RGBA", (500, 500), (255,200,50,0))
# img = Image.new("RGBA", (500, 500), (0,255,255,60))
# img = Image.new("RGBA", (500, 500))
ImageDraw.Draw(img).ellipse((200,200,300,300), fill=(255,155,60,255))
img = img.filter(ImageFilter.GaussianBlur(10))
img.show()
img.save("../output/halo1.png")