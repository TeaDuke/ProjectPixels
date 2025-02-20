import datetime
import json
import shutil
import os

from PIL import Image
import pickle

from openpyxl.descriptors import DateTime


class ImagePP:

    PATH = 'data\\images\\'
    PR_OR = "i-or" # original file
    PR_CO = "i-co" # colored file

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

    # Set settings when image is added at first time
    def first_settings(self, ipath):
        img = Image.open(ipath)
        self.id = datetime.datetime.now().day.__str__() # TODO: make it differently
        parts = img.filename.split('/')
        self.name = parts[len(parts)-1]
        self.iformat = img.format.lower()
        self.copy_image_to_local_folder(ipath)

        self.height, self.width = img.height, img.width
        self.pixels = self.height * self.width
        self.colored_pixels = 0

        self.write_data_to_data_file()
        self.create_progress_image()

    # copy image from ipath to local folder, rename it
    def copy_image_to_local_folder(self, ipath):
        shutil.copy(ipath, self.PATH)
        os.rename(f"{self.PATH}{self.name}",f"{self.PATH}i{self.id}.{self.iformat}")

    # create empty progress image
    def create_progress_image(self):
        pimg = Image.new("RGBA", (self.width, self.height), (255,255,255,0))
        pimg.save(f"{self.PATH}p{self.id}.png")

    # save data from image to data file at first time
    def write_data_to_data_file(self):
        with open(f"{self.PATH}d{self.id}.data", 'wb') as f:
            pickle.dump(json.dumps(self.__dict__), f)
            print(json.dumps(self.__dict__))

    # If class got ID of image, this functions is executed to read data
    def read_data_from_data_file(self):
        with open(f"{self.PATH}d{self.id}.data", 'rb') as f:
            data = json.loads(pickle.load(f))
            self.name = data['name']
            self.iformat = data['iformat']
            self.height = data['height']
            self.width = data['width']
            self.pixels = data['pixels']
            self.colored_pixels = data['colored_pixels']
