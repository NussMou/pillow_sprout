from PIL import Image, ImageDraw, ImageFilter
img = Image.new("RGBA", (200, 200), (0,0,0,0))
ImageDraw.Draw(img).ellipse((20,20,180,180), fill=(255,0,0,255))
img = img.filter(ImageFilter.GaussianBlur(10))
img.show()
img.save("../output/halo.png")