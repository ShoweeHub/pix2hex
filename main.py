from PIL import Image

image = Image.open('weibo.png')
w, h = image.size
pixels = list(image.getdata())
for y in range(h):
    print("{", end='')
    for x in range(w):
        print('0x%02X%02X%02X%s' % (pixels[y * w + x][0], pixels[y * w + x][1], pixels[y * w + x][2], ',' if x < w - 1 else ''), end='')
    print("}%s" % (',' if y < h - 1 else ''))
