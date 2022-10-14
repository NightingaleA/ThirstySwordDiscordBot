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

    self.dictionary = self._commandsDataframe.to_dict(orient="index")
    self.list = []

    for id, element in self.dictionary.items():
      command = Command(id,element['english'],element['español'], element['type'], element['status'])
      self.list.append(command)

  def get_command_list(self, localizer, message, commands_to_include):
    notation_needed = False;
    response = ''
    title = ''
    
    if 'command_label_list' in commands_to_include:
      label_list = self.__get_label_list__(localizer)
      response, title, notation_needed = self.__get_formated_list__(localizer, response, label_list, notation_needed)

    if  'command_condition_list' in commands_to_include:
      condition_list = self.__get_condition_list__(localizer)
      response, title, notation_needed = self.__get_formated_list__(localizer, response, condition_list, notation_needed)

    if 'command_basic_move_list' in commands_to_include:
      basic_list = self.__get_basic_list__(localizer)
      response, title, notation_needed = self.__get_formated_list__(localizer, response, basic_list, notation_needed)
    
    if 'command_special_move_list' in commands_to_include:
      special_list = self.__get_special_list__(localizer)
      response, title, notation_needed = self.__get_formated_list__(localizer, response, special_list, notation_needed)

    if 'command_playbook_list' in commands_to_include:
      playbook_list = self.__get_playbook_list__(localizer)
      response, title, notation_needed = self.__get_formated_list__(localizer, response, playbook_list, notation_needed)

    if 'command_help_list' in commands_to_include:
      help_list = self.__get_help_list__()
      help, title, notation_needed = self.__get_formated_list__(localizer, response, help_list,notation_needed)
      
    if(notation_needed):
      response = response + "\n\n" + self.formatter.notation + localizer.get_utils_with_key("notation_explanation")

    embed = discord.Embed(title=title, colour=5450873)
    author = message.author
    embed.set_author(name=author.display_name)
    embed.set_thumbnail(url=author.avatar)
    embed.add_field(name='**—————————**', value=response)
   
    return (embed)

  def __get_help_list__(self):
    help_list = [ ]
    for command in self.list:
      if(command.type == "command_help_list"):
        help_list.append(command)
    return help_list

  def __get_label_list__(self,localizer):
    label_list = []
    for label in self.list:
      if(label.type == "command_label_list"):
        label_list.append(label)
      if(label.type == "command_label"):
         label_list.append(label)
      
    return label_list

  def __get_condition_list__(self,localizer):
    condition_list = []
    for condition in self.list:
      if(condition.type == "command_condition_list"):
        condition_list.append(condition)
      if(condition.type == "command_condition"):
         condition_list.append(condition)
      
    return condition_list

  def __get_basic_list__(self,localizer):
    basic_list =[]
    for basic in self.list:
      if(basic.type == "command_basic_move_list"):
        basic_list.append(basic)
      if(basic.type == "command_basic_move"):
         basic_list.append(basic)
      
    return basic_list

  def __get_special_list__(self,localizer):
    special_list = []
    for special in self.list:
      if(special.type == "command_special_move_list"):
        special_list.append(special)
      if(special.type == "command_special_move"):
         special_list.append(special)
    return special_list

  def __get_playbook_list__(self,localizer):
    playbook_list = []
    for playbook in self.list:
      if(playbook.type == "command_playbook_list"):
        playbook_list.append(playbook)
      if(playbook.type == "command_playbook"):
         playbook_list.append(playbook)
      
    return playbook_list

  def get_command(self, localizer, key):
    return self.dictionary[key][localizer.lang.name]

  def __get_formated_list__(self, localizer, response, list,_notation_needed):
    cmd = ''
    title = '' 
    new_response = response
    notation_needed = _notation_needed
    if(list[0].status == "added"):
      cmd = (self.formatter.bold + self.formatter.newline).format( list[0].languages[localizer.lang.name])
    else:
      cmd = (self.formatter.notation + self.formatter.bold + self.formatter.newline).format( list[0].languages[localizer.lang.name])
      notation_needed = True
      
    new_response = new_response + cmd
    title = localizer.get_utils_with_key('asking_for') + cmd
    list.pop(0)
    index = 0;
    for label in list:
      if(index>0):
        new_response = new_response + ", "
      index +=1
      cmd = ''
      if(label.status == COMMAND_STATUS.added.name):
        cmd = (self.formatter.italics).format(label.languages[localizer.lang.name])
      else:
        cmd = (self.formatter.notation + self.formatter.italics).format(label.languages[localizer.lang.name])
        notation_needed = True

      new_response = new_response + cmd
    
    new_response = new_response + '\n'
    return new_response, title, notation_needed

  
