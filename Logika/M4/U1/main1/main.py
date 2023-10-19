from PIL import Image, ImageFilter

with Image.open('ryan_gosling.JPEG') as original:
    print(original.size)
    print(original.format)
    print(original.mode)

    bw_original = original.convert('L')
    bw_original.show()
    bw_original.save('ryan_gosling.JPEG')

    blur = original.filter(ImageFilter.BLUR)
    blur.show()

    picup = original.transpose(Image.ROTATE_180)
    picup.show()
    picup.save('ryan_gosling.JPEG')