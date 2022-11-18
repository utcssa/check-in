from PIL import Image, ImageFont, ImageDraw
from qrcode import QRCode
import pandas as pd
import os


URL_BASE = 'https://check-in.utcssa.net/'


def make_image(uuid, num):
    # create QR code
    qr = QRCode()
    qr.add_data(URL_BASE + uuid)

    # create main image
    main = Image.new(mode='RGB', size=(750, 750), color='#eee')
    main.paste(qr.make_image(), box=(150, 150))

    draw = ImageDraw.Draw(main)

    # draw upper text
    t1 = '''\
    扫码签到参与抽奖
    Check in for Prize Entry'''
    f1 = ImageFont.truetype('OPPOSans-R.ttf', 32)
    draw.multiline_text((750 / 2, 75), t1, '#000', font=f1, align='center', anchor='mm')

    # draw lower text
    t2 = f'No. {int(num):03}'
    f2 = ImageFont.truetype('OPPOSans-R.ttf', 48)
    draw.text((750 / 2, 750 - 75), t2, '#000', font=f2, anchor='mm')
    
    return main


# make directory to store images
# if directory already exists please remove
try:
    os.mkdir('images')
except:
    print('Failed to create images directory. Please check if it already exists.')
    exit(1)

    
# make images
for _, row in pd.read_csv('uuid.csv').iterrows():
    _id = row['_id']
    img_path = os.path.join('images', f'img-{_id:03}.jpg')
    
    img = make_image(row['uuid'], _id)
    img.save(img_path)
