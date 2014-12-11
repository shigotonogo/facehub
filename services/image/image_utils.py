from PIL import Image
import io
import uuid
import urllib.request

def crop_image(image_src, x, y, width, height, scale = 1):
    image = Image.open(io.BytesIO(urllib.request.urlopen(image_src).read()))
    croped =image.crop((int(x), int(y), int(x) + int(width), int(y) + int(height)))
    resized = image.resize((int(width) * scale, int(height) * scale), Image.NEAREST)
    resized.save("/tmp/testimg.jpg")