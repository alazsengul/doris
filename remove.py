import os
import PIL
import pdf2image

# dots per inch (dpi) adjusts quality and file size

images = pdf2image.convert_from_path('lurie.pdf', dpi = 600)
images[0].save("out.pdf", save_all = True, append_images = images[1:], subsampling=0, quality=100)
