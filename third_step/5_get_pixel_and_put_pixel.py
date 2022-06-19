from PIL import Image
def r2(x):
    return int((x ** 0.7) * 10)


img = Image.open("../assets/evening1.jpg")
img.show()
width,height = img.size

for w in range(width):
    for h in range(height):
        r, g, b = img.getpixel((w, h))
        r = r2(r)
        g = r2(g)
        b = r2(b)
        img.putpixel((w, h), (r, g, b))
img.show()