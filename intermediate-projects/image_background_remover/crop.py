from PIL import Image

# img = Image.open('finalyr.png')
img = Image.open('result11.tif')

width, height = img.size

dx = int(width/4)
dy = int(height/4)
x = 800  # 360
y = 370  # 140
x1 = x + 30  # 60
y1 = y + 30

# print(f'width = {width} height ={height}')
# im1 = img.crop((left, top, right, bottom))
im1 = img.crop((x, y, width-x1, height - y1))  # y+height


# im1.save("./crop.png", "PNG")
# Shows the image in image viewer
im1.show()
