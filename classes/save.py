import json
import pickle
import os.path
from enums.status import Status

class Save:
   PATH_SAVE = "data\\config_save.data"

   _status = Status.ABSENT.value

   _id = ""
   _name = ""
   _images_id = []
   _current_image_index = None
   _work = []
   _work_history = None

   @staticmethod
   def read_save():

      if os.path.exists(Save.PATH_SAVE):
         Save._status = Status.EXIST
         with open(Save.PATH_SAVE, 'rb') as f:
            data = json.loads(pickle.load(f))
            Save._id = data['id']
            Save._name = data['name']
            Save._images_id = data['image_id']
            Save._current_image_index = data['current_image_index']
            Save._work = data['work']
            Save._work_history = data['work_history']
         Save._data_validation()

   @staticmethod
   def _data_validation():
      # TODO: finish this function after finish all classes.
      print("data validation is not finished, do something with it!")


   @staticmethod
   def get_current_image_id():
      return Save._images_id[Save._current_image_index]

   @staticmethod
   def get_last_image_id():
      return Save._images_id[len(Save._images_id.count)-1]

   @staticmethod
   def get_save_name():
      return Save._name

   @staticmethod
   def get_status():
      return Save._status