import pandas as pd
import discord
from collections import namedtuple

command_tructure = namedtuple('command', ['id', 'english', 'español', 'type'])


class Commands:

  def __init__(self):
    self._commandsDataframe = pd.read_csv(
      "ThirstySword/Data/data_commands.csv")
    self._commandsDataframe.set_index("localization_id",
                                      drop=True,
                                      inplace=True)

    self.dictionary = self._commandsDataframe.to_dict(orient="index")
    self.list = []

    for id, element in self.dictionary.items():
      self.list.append(
        command_tructure(id, element['english'], element['español'],
                         element['type']))

  def get_list(self, lang, message):
    commands = self._commandsDataframe[lang.name]
    commands_list = commands.tolist()

    response = ''
    embed = discord.Embed(title="Commands:", colour=5450873)
    author = message.author
    embed.set_author(name=author.display_name)
    embed.set_thumbnail(url=author.avatar)
    for command in commands_list:
      cmd = ("**{}**\n").format(command)
      response = response + cmd

    embed.add_field(name='**—————————**', value=response)
    return (embed)
