import pandas as pd
import discord
from Data.command import Command, COMMAND_STATUS
from Utils.text_formatter import Text_Formatter


class Commands_Manager:

  def __init__(self):
    self.formatter = Text_Formatter()
    self._commandsDataframe = pd.read_csv(
      "ThirstySword/Data/data_commands.csv")
    self._commandsDataframe.set_index("localization_id",
                                      drop=True,
                                      inplace=True)

    self._commandsDataframe.fillna('-', inplace=True)

    self.dictionary = self._commandsDataframe.to_dict(orient="index")
    self.list = []

    for id, element in self.dictionary.items():
      command = Command(id, element['english'], element['español'],
                        element['type'], element['status'])
      self.list.append(command)

#Lists Handling

  def get_command_list(self, data_manager, commands_to_include):
    notation_needed = False
    response = self.formatter.newline
    title = ''
    footer = ''

    for command_type in commands_to_include:
      list_of_commands = self.__get_list__(command_type)
      response, title, notation_needed = self.get_formated_list(
        data_manager.localizer, response, title, list_of_commands, notation_needed)
      response = response + self.formatter.newline

    if (notation_needed):
      footer = self.formatter.newline + self.formatter.newline + self.formatter.notation + data_manager.localizer.get_utils_with_key(
        "notation_explanation")

    embed = discord.Embed(title=title, colour=5450873, description=response)
    if (footer):
      embed.set_footer(text=footer)
    embed.set_author(name= data_manager.current_command.user_display_name )
    embed.set_thumbnail(url= data_manager.current_command.avatar)

    return (embed)

  def __get_list__(self, list_type):
    list = []
    for command in self.list:
      if (command.type == list_type):
        list.append(command)
    return list

  def get_playbook_move_list(self, data_manager, playbook_id):
    list = []
    for command in self.list:
      if (command.type == data_manager.COMMAND_TYPE.command_playbook_move.name
          or command.type
          == data_manager.COMMAND_TYPE.command_basic_move_extended.name):
        if (playbook_id in command.id):
          list.append(command)
    return list

  def get_formated_list(self, localizer, response, title, list,
                        _notation_needed):
    cmd = ''
    new_response = response
    notation_needed = _notation_needed

    index = 0
    is_list = False
    for command in list:
      if (index > 0):
        new_response = new_response + ", "
      index += 1
      cmd = ''

      if ('list' in command.type):
        is_list = True
        if (command.status == "added"):
          cmd = command.languages[localizer.lang.name]
        else:
          cmd = self.formatter.notation +  command.languages[localizer.lang.name]
          notation_needed = True

        if not title:
          title = localizer.get_utils_with_key('asking_for') + (
            self.formatter.bold).format(cmd)
        else:
          new_response = new_response + (
            self.formatter.bold_underline).format(cmd)
      else:
        if (command.status == COMMAND_STATUS.added.name):
          cmd = (self.formatter.italics).format(
            command.languages[localizer.lang.name])
        else:
          cmd = (self.formatter.notation + self.formatter.italics).format(
            command.languages[localizer.lang.name])
          notation_needed = True
        new_response = new_response + cmd

    if not is_list:
      new_response = new_response + self.formatter.newline

    return new_response, title, notation_needed


#Command Handling

  def get_command_with_key(self, localizer, key):
    return self.dictionary[key][localizer.lang.name]
