import pandas as pd
import discord
from collections import namedtuple
from Data.move import Move

class Moves:
  def __init__(self):
    self._movesDataframe = pd.read_csv(
      "ThirstySword/Data/data_moves.csv")
    self._movesDataframe.set_index("uniqueID",
                                      drop=True,
                                      inplace=True)

    self.dictionary = self._movesDataframe.to_dict(orient="index")
    self.list = []

    for id, element in self.dictionary.items():
      move = Move(id, element['command'], element['name'], element['trigger'], element['blurb'], element['rolls'], element['type'])
      self.list.append(move)

  def do_move(self, data_manager, message):
    move_to_do = None
    for move in self.list:
      if(data_manager.current_command.id == move.command):
        move_to_do = move
        break

    if(move_to_do):
      response = move_to_do.parse_move(data_manager, message)  
      return response
      

    
