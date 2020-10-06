#!/usr/bin/env python3

# google it automation specialist w/ python certification via Coursera
# github.com/justisGipson
# Oct 6, 2020

from PIL import Image
from glob import glob
import os

# script lives in images folder

# iterate through each file and ignore hidden file (images/DStore)
for file in glob('ic_*'):
    image = Image.open(file).convert('RGB')
    '''
    * rotate image 90deg clockwise
    * resize to 128x128
    * save image in new folder, jpeg format
    '''
    path, filename = os.path.split(file)
    filename = os.path.splitext(filename)[0]
    image.rotate(270).resize((128, 128)).save('/opt/icons/{}.jpeg'.format(filename))

print('Done')
