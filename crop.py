from PIL import Image
from datetime import datetime
from time import sleep
import glob


def crop_center(org_img, width, height):
    img_width, img_height = img.size

    return org_img.crop(((img_width - width) // 2,
                         (img_height - height) // 2,
                         (img_width + width) // 2,
                         (img_height + height) // 2))


def crop_square(org_img):
    return crop_center(org_img, min(img.size), min(img.size))


files = glob.glob('./images/*')

for file_name in files:

    if file_name.endswith(('.png', '.jpeg', '.jpg')):
        img = Image.open(file_name)
        img = crop_square(img)
        time = datetime.now().strftime('%Y%m%d%H%M%S')
        path = './cropimages/' + time + '.jpg'
        img.save(path, 'JPEG', quality=100, optimize=True)

        sleep(1)
