import pandas as pd
import discord
from Data.move import Move

class Moves_Manager:
  def __init__(self):
    self._movesDataframe = pd.read_csv(
      "ThirstySword/Data/data_moves.csv")
    self._movesDataframe.set_index("uniqueID",
                                      drop=True,
                                      inplace=True)
    self._movesDataframe.fillna('-', inplace=True)
    self.dictionary = self._movesDataframe.to_dict(orient="index")
    self.list = []

    for id, element in self.dictionary.items():
      move = Move(id, element['command'], element['name'], element['trigger'], element['blurb'], element['rolls'], element['type'])
      self.list.append(move)

  def do_move(self, data_manager):
    move_to_do = self.get_move(data_manager.current_command.id)

    if(move_to_do):
      response = move_to_do.parse_move(data_manager)  
      return response

  def get_move(self, command_id):
    for move in self.list:
      if(command_id == move.command):
        return move
        

    
