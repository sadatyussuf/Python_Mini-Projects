from PIL import Image


def crop_image():
    img = Image.open('New.tif')
    width, height = img.size
    x = 830  # 800 360
    y = 400  # 370 140
    x1 = x + 30  # 60
    y1 = y + 30
    im1 = img.crop((x, y, width-x1, height - y1))  # y+height
    im1.save("./crop.tif", "TIFF")
    # print(cc)

    # return im1.save("./crop.png", "PNG")


def image_converter():
    # img = Image.open('test5.tif')
    img = Image.open('./crop.tif')
    img = img.convert("RGBA")
    data = img.getdata()

    newData = []
    for item in data:
        # print(item)
        if item[0] <= 155 and item[1] <= 155 and item[2] <= 155:
            # newData.append((255, 255, 255, 0))
            newData.append((255, 0, 0, 255))
            # newData.append((255, 255, 255, 0))
        else:
            # continue
            # newData.append(item)
            newData.append((255, 255, 255, 0))

    img.putdata(newData)
    img.save("./result.tif", "TIFF")
    print("Successful")
    print(len(newData))
    # print(newData)


crop_image()
image_converter()
