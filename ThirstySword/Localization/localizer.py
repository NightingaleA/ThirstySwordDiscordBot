import pandas as pd
from enum import Enum

class Localizer:
  LANGUAGES = Enum('LAGUAGES', 'none english español')
  def __init__(self):
    self.lang  = self.LANGUAGES.english
    self.__load_condtions__()
    self.__load_labels__()
    self.__load_moves__()
    self.__load_playbooks__()
    self.__load_utils__()

  def __load_condtions__(self):
    self._condition_dataframe = pd.read_csv(
      "ThirstySword/Localization/localization_conditions.csv")
    self._condition_dataframe.set_index("localization_id",
                                      drop=True,
                                      inplace=True)

    self.dictionary_conditions = self._condition_dataframe.to_dict(orient="index")

  def __load_labels__(self):
    self._labels_dataframe = pd.read_csv(
      "ThirstySword/Localization/localization_labels.csv")
    self._labels_dataframe.set_index("localization_id",
                                      drop=True,
                                      inplace=True)

    self.dictionary_labels = self._labels_dataframe.to_dict(orient="index")

  def __load_moves__(self):
    self._moves_dataframe = pd.read_csv(
      "ThirstySword/Localization/localization_moves.csv")
    self._moves_dataframe.set_index("localization_id",
                                      drop=True,
                                      inplace=True)

    self.dictionary_moves = self._moves_dataframe.to_dict(orient="index")

  def __load_playbooks__(self):
    self._playbooks_dataframe = pd.read_csv(
      "ThirstySword/Localization/localization_playbooks.csv")
    self._playbooks_dataframe.set_index("localization_id",
                                      drop=True,
                                      inplace=True)

    self.dictionary_playbooks = self._playbooks_dataframe.to_dict(orient="index")

  def __load_utils__(self):
    self._utils_dataframe = pd.read_csv(
      "ThirstySword/Localization/localization_utils.csv")
    self._utils_dataframe.set_index("localization_id",
                                      drop=True,
                                      inplace=True)

    self.dictionary_utils = self._utils_dataframe.to_dict(orient="index")


  def get_conditon_with_key(self, key):
    return self.dictionary_conditions[key][self.lang.name]
  
  def get_label_with_key(self, key):
    return self.dictionary_labels[key][self.lang.name]

  def get_move_with_key(self, key):
    return self.dictionary_moves[key][self.lang.name]

  def get_playbook_with_key(self, key):
    return self.dictionary_playbooks[key][self.lang.name]

  def get_utils_with_key(self, key):
    return self.dictionary_utils[key][self.lang.name]

   
