import datetime
import json

from PIL import Image
import pickle

from openpyxl.descriptors import DateTime


class ImagePP:

    PATH = 'data\\images\\'
    PR_OR = "i-or" # original file
    PR_CO = "i-co" # colored file

    id = ''
    name = ''
    height, width = 0, 0
    pixels = 0
    colored_pixels = 0

    def __init__(self, ipath='', id=''):
        if not ipath == '':
            self.FirstSettings(ipath)
        if not id == '':
            self.id = id
            self.ReadDataFromDataFile()
        print("class ImagePP is created")
        pass

    def FirstSettings(self, ipath):
        img = Image.open(ipath)
        self.id = "i" + datetime.datetime.now().day.__str__()
        self.name = img.filename
        self.height, self.width = img.height, img.width
        self.pixels = self.height * self.width
        self.WriteDataToDateFile()

    def ReadDataFromDataFile(self):
        with open(self.PATH + 'd-' + self.id + ".data", 'rb') as f:
            data = pickle.load(f)
            print(data) # TODO: finish it

    def WriteDataToDateFile(self):
        with open(self.PATH + 'd-' + self.id + ".data", 'wb') as f:
            pickle.dump(json.dumps(self.__dict__), f)
            print(json.dumps(self.__dict__))


