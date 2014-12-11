from PIL import Image
import io
import urllib

def crop_image(image_src, x, y, width, height, scale = 1):
    image = Image.open(io.BytesIO(urllib.urlopen(image_src).read()))
    image.crop((int(x), int(y), int(x) + int(width), int(y) + int(height)))
    image.resize((int(width) * scale, int(height) * scale), Image.NEAREST)
    tmpImage= "/tmp%s" % uuid.uuid4()
    image.save(tmpImage)
    return tmpImage
