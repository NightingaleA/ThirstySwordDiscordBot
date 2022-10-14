import pandas as pd
import discord
from collections import namedtuple

move_structure = namedtuple('move', ['id', 'command', 'name', 'trigger', 'blurb', 'rolls', 'type'])

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
      self.list.append(
        move_structure(id, element['command'], element['name'],
                         element['trigger'],
                         element['blurb'],
                         element['rolls'],
                         element['type']))

  def get_list(self,command_type, data_manager, message):
    moves = (self._movesDataframe[self._movesDataframe["type"] == command_type.name] )
    moves_list = moves["command"].tolist()
    print(moves_list)
    response = ''
    embed = discord.Embed(title=data_manager.localizer.get_move_with_key('title_basic_moves'), colour=5450873)
    author = message.author
    embed.set_author(name=author.display_name)
    embed.set_thumbnail(url=author.avatar)
    index = 0
    for command in moves_list:
      if(index>0):
        response = response + ", "
      index +=1
      cmd = ("**{}**").format(data_manager.commands.get_command(data_manager.localizer,command))
      response = response + cmd

    embed.add_field(name='**—————————**', value=response)
    return (embed)