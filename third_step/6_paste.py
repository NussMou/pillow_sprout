from PIL import Image,ImageFilter

Image1 = Image.open('../assets/evening1.jpg')

Image1copy = Image1.copy()
Image2 = Image.open('../assets/evening2.jpg')
Image2copy = Image2.copy()

Image1copy.paste(Image2copy, (500, 500))
img = Image1copy.filter(ImageFilter.GaussianBlur(50))
Image1copy.show()
Image1copy.save('../output/pasted2.png')

