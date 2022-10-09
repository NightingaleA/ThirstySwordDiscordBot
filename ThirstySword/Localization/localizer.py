import pandas as pd
from enum import Enum
from collections import namedtuple

class Localizer:
  LANGUAGES = Enum('LAGUAGES', 'none english español')
  localization_structure = namedtuple('localization_key', ['id', 'english', 'español'])
  
  def __init__(self):
    self.lang  = self.LANGUAGES.english
    self.__load_condtions__
    self.__load_labels__
    self.__load_moves__
    self.__load_playbooks__

  def __load_condtions__(self):
    self._conditionsDataframe = pd.read_csv(
      "ThirstySword/Data/localization_conditions.csv")
    self._conditionsDataframe.set_index("localization_id",
                                      drop=True,
                                      inplace=True)

    self.dictionary = self._conditionsDataframe.to_dict(orient="index")

  def __load_labels__(self):
    self._labelsDataframe = pd.read_csv(
      "ThirstySword/Data/localization_labels.csv")
    self._labelsDataframe.set_index("localization_id",
                                      drop=True,
                                      inplace=True)

    self.dictionary = self._labelsDataframe.to_dict(orient="index")

  def __load_moves__(self):
    self._movesDataframe = pd.read_csv(
      "ThirstySword/Data/localization_moves.csv")
    self._movesDataframe.set_index("localization_id",
                                      drop=True,
                                      inplace=True)

    self.dictionary = self._movesDataframe.to_dict(orient="index")

  def __load_playbooks__(self):
    self._playbooksDataframe = pd.read_csv(
      "ThirstySword/Data/localization_playbooks.csv")
    self._playbooksDataframe.set_index("localization_id",
                                      drop=True,
                                      inplace=True)

    self.dictionary = self._playbooksDataframe.to_dict(orient="index")

  def get_conditon_with_key(self, key):
    return self.__conditionsDataframe[self.lang][key]
  
  def get_label_with_key(self, key):
    return self._labelsDataframe[self.lang][key]

  def get_move_with_key(self, key):
    return self._movesDataframe[self.lang][key]

  def get_playbook_with_key(self, key):
    return self._playbooksDataframe[self.lang][key]

   
