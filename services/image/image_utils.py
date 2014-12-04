from PIL import Image
import io
import urllib.request

def crop_image(image_src, x, y, width, height, scale = 1):
    image = Image.open(io.StringIO(urllib.request.urlopen(image_src).read()))
    image.crop((x, y, x + width, y + height))
    image.resize((width * scale, height * scale), Image.NEAREST)
    image.save("/tmp/test-image.png")
