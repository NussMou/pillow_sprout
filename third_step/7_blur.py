from PIL import Image, ImageDraw, ImageFilter
img = Image.new("RGBA", (5000, 5000), (0,0,0,255))
ImageDraw.Draw(img).ellipse((2000,2000,3000,3000), fill=(0,0,0,0))
img = img.filter(ImageFilter.GaussianBlur(50))
img.show()
img.save("../output/blur_circle.png")