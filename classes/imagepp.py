import datetime
import json
import shutil
import os

from PIL import Image, ImageDraw
import pickle

from openpyxl.descriptors import DateTime


class ImagePP:
    PATH = 'data\\images\\'
    # prefixes for different files

    PD = 'd'
    PI = 'i'
    PPI = 'p'

    id = ''
    name = ''
    iformat = ''
    height, width = 0, 0
    pixels = 0
    colored_pixels = 0

    # constructor
    def __init__(self, ipath='', id=''):
        if ipath != '':
            self.first_settings(ipath)
        elif id != '':
            self.id = id
            self.read_data_from_data_file()
        else:
            print("You forget to send ID or IPATH to Image class!")
        print("class ImagePP is created")
        pass

    #region First setup
    # Set settings when image is added at first time
    def first_settings(self, ipath):
        img = Image.open(ipath)
        self.id = datetime.datetime.now().day.__str__()  # TODO: make it differently
        parts = img.filename.split('/')
        self.name = parts[len(parts) - 1]
        self.iformat = img.format.lower()
        self.copy_image_to_local_folder(ipath)

        self.height, self.width = img.height, img.width
        self.pixels = self.height * self.width
        self.colored_pixels = 0

        self.save_data_to_data_file()
        self.create_progress_image()

    # copy image from ipath to local folder, rename it
    def copy_image_to_local_folder(self, ipath):
        shutil.copy(ipath, self.PATH)
        os.rename(f"{self.PATH}{self.name}", f"{self.PATH}{self.PI}{self.id}.{self.iformat}")

    # create empty progress image
    def create_progress_image(self):
        pimg = Image.new("RGB", (self.width, self.height), (255, 255, 255))
        pimg.save(f"{self.PATH}{self.PPI}{self.id}.png")

    #endregion First setup

    # If class got ID of image, this functions is executed to read data
    def read_data_from_data_file(self):
        with open(f"{self.PATH}{self.PD}{self.id}.data", 'rb') as f:
            data = json.loads(pickle.load(f))
            self.name = data['name']
            self.iformat = data['iformat']
            self.height = data['height']
            self.width = data['width']
            self.pixels = data['pixels']
            self.colored_pixels = data['colored_pixels']

    # save data from image to data file at first time
    def save_data_to_data_file(self):
        with open(f"{self.PATH}{self.PD}{self.id}.data", 'wb') as f:
            pickle.dump(json.dumps(self.__dict__), f)
            print(json.dumps(self.__dict__))

    # colore pixels in progres image
    def colore_pixels(self, count):
        img = self.get_original_image().convert("RGB")
        pimg = Image.open(f"{self.PATH}{self.PPI}{self.id}.png")
        draw = ImageDraw.Draw(pimg)

        sty = self.colored_pixels // self.width
        stx = self.colored_pixels % self.width

        for i in range(sty, self.height):
            for j in range(stx, self.width):
                r = g = b = 0
                # rgb = []
                # if self.iformat == 'jpeg': # JPEG format
                #     r, g, b = img.getpixel((j, i))
                # else: # PNG format
                #     rgb = img.getpixel((j, i))
                r, g, b = img.getpixel((j, i))
                draw.polygon([(j,i), (j,i)], fill=(r, g, b), outline=None, width=0)
                count-=1
                self.colored_pixels+=1
                if count == 0: break
            stx = 0
            if count == 0: break

        self.save_data_to_data_file()
        pimg.save(f"{self.PATH}{self.PPI}{self.id}.png")

    def get_original_path(self):
        return f"{self.PATH}{self.PI}{self.id}.{self.iformat}"
