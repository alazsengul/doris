import os
import PIL
import pdf2image
from tqdm import tqdm
from collections import defaultdict

# dots per inch (dpi) adjusts quality and file size
images = pdf2image.convert_from_path('files/lurie.pdf', dpi = 300)

# figure out watermark colors
im = images[0]

im_width, im_height = im.size
pixels = im.load()

colors_to_freq = defaultdict(int)

for y in range(im_height):

    line_pixels = set()

    contains_black = False

    for x in range(im_width):

        current_pixel = im.getpixel((x, y))

        if current_pixel == (0, 0, 0):
            contains_black = True
            break
        else:
            line_pixels.add(current_pixel)

    if not contains_black:
        no_white = line_pixels - set([(255, 255, 255)])

        if no_white:
            colors_to_freq[tuple(list(no_white))] += 1

watermark_colors = set(list(sorted(colors_to_freq, key = colors_to_freq.get, reverse = True)[0]))

print(watermark_colors)




for y in range(im_height):

    for x in range(im_width):

        if im.getpixel((x, y)) in watermark_colors:
            pixels[x, y] = (255, 255, 255)


im.save("files/out.jpg", subsampling=0, quality=100)








# for im in tqdm(images[:1], desc = "Images: "):


            #if im.getpixel((w, h)) != (0, 0, 0):
            #    pixels[w, h] = (255, 255, 255)

# images[0].save("files/out.pdf", save_all = True, append_images = images[1:], subsampling=0, quality=100)
