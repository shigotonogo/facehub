from PIL import Image
import io
import uuid
import urllib.request
import string
import random

def crop_image(image_src, image_width, x, y, width, height):
    tmp = __tmp_file_name()
    image = Image.open(io.BytesIO(urllib.request.urlopen(image_src).read()))
    origin_width = image.size[0]
    scale_size = origin_width / int(image_width)
    croped =image.crop((int(x*scale_size), int(y*scale_size), int(scale_size*(x + width)), int(scale_size*(y + height))))
    resized = image.resize((600,800), Image.NEAREST)
    croped.save(tmp)
    return tmp

def __tmp_file_name(size=6, chars=string.ascii_uppercase + string.digits):
   return "/tmp/%s.png" % (''.join(random.choice(chars) for _ in range(size)))