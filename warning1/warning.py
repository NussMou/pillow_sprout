from PIL import Image

frames = []
for i in range(10):
    num = str(i)
    tmp = "warning1_0000"+num+".png"
    a = Image.open(tmp)
    frames.append(a)
for i in range(11,50):
    num = str(i)
    tmp = "warning1_000"+num+".png"
    a = Image.open(tmp)
    frames.append(a)

frames = [frame.convert('PA') for frame in frames]

frames[0].save('test.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=200, loop=0, transparency=0)