import json
import random

from PIL import Image
import numpy as np
from PyQt6.QtGui import QImage


def start():
    # close_pixels()
    img = QImage(f"C:\\Users\\maxch\\Documents\\projects\\ProjectPixels\\data\\ghibli.jpg")
    print(img.width())
    img.save("test.png")

def close_pixels():
    img = Image.open("pimg.png").convert("RGBA")

    # data = np.array(img)
    #
    # data[:,:,3] = 255
    #
    # img = Image.fromarray(data, "RGBA")
    # img.save("ppimg.png")

def create_array_closed_pixels():
    img = Image.open("pimg.png").convert("RGBA")

    data = np.array(img)

    tp = list(zip(*np.where(data[:,:,3] == 0)))
    random.shuffle(tp)
    return tp

if __name__ == '__main__':
    start()