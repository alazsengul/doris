import os
import PIL
import pdf2image
from tqdm import tqdm

# dots per inch (dpi) adjusts quality and file size

images = pdf2image.convert_from_path('files/lurie.pdf', dpi = 300)

for im in tqdm(images, desc = "Images: "):

    im_width, im_height = im.size
    pixels = im.load()

    for w in tqdm(range(1, im_width), desc = "Pixels: "):
        for h in range(1, im_height):

            if im.getpixel((w, h)) != (0, 0, 0):
                pixels[w, h] = (255, 255, 255)

images[0].save("files/out.pdf", save_all = True, append_images = images[1:], subsampling=0, quality=100)
