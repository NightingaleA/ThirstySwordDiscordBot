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

  def get_full_list(self, localizer, message):
    notation_needed = False;
    response = ''
    embed = discord.Embed(title="Commands:", colour=5450873)
    author = message.author
    embed.set_author(name=author.display_name)
    embed.set_thumbnail(url=author.avatar)
    
    help_list = self.__get_help_list__()
    cmd = (self.formatter.bold + self.formatter.newline).format( help_list[0].languages[localizer.lang.name])
    response = response + cmd

    label_list = self.__get_label_list__(localizer)
    cmd = ''
    if(label_list[0].status == "added"):
      cmd = (self.formatter.bold + self.formatter.newline).format( label_list[0].languages[localizer.lang.name])
    else:
      cmd = (self.formatter.notation + self.formatter.bold + self.formatter.newline).format( label_list[0].languages[localizer.lang.name])
      notation_needed = True
      
    response = response + cmd
    label_list.pop(0)
    index = 0;
    for label in label_list:
      if(index>0):
        response = response + ", "
      index +=1
      cmd = ''
      if(label.status == COMMAND_STATUS.added.name):
        cmd = (self.formatter.italics).format(label.languages[localizer.lang.name])
      else:
        cmd = (self.formatter.notation + self.formatter.italics).format(label.languages[localizer.lang.name])
        notation_needed = True

      response = response + cmd

    condition_list = self.__get_condition_list__(localizer)
    cmd = ("\n**{}**\n").format( condition_list[0])
    response = response + cmd
    condition_list.pop(0)
    index = 0;
    for condition in condition_list:
      if(index>0):
        response = response + ", "
      index +=1
      cmd = ("*{}*").format(condition)
      response = response + cmd

    basic_list = self.__get_basic_list__(localizer)
    cmd = ("\n**{}**\n").format( basic_list[0])
    response = response + cmd
    basic_list.pop(0)
    index = 0;
    for basic in basic_list:
      if(index>0):
        response = response + ", "
      index +=1
      cmd = ("*{}*").format(basic)
      response = response + cmd

    special_list = self.__get_special_list__(localizer)
    cmd = ("\n**{}**\n").format( special_list[0])
    response = response + cmd
    special_list.pop(0)
    index = 0;
    for special in special_list:
      if(index>0):
        response = response + ", "
      index +=1
      cmd = ("*{}*").format(special)
      response = response + cmd

    playbook_list = self.__get_playbook_list__(localizer)
    cmd = ("\n**{}**\n").format( playbook_list[0])
    response = response + cmd
    playbook_list.pop(0)
    index = 0;
    for playbook in playbook_list:
      if(index>0):
        response = response + ", "
      index +=1
      cmd = ("*{}*").format(playbook)
      response = response + cmd



    if(notation_needed):
      response = response + "\n\n" + self.formatter.notation + localizer.get_utils_with_key("notation_explanation")
      
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
    condition = self._commandsDataframe[self._commandsDataframe["type"] == "command_condition_list"]
    condition_list = condition[localizer.lang.name].tolist()

    condition = self._commandsDataframe[self._commandsDataframe["type"] == "command_condition"]
    for label in condition[localizer.lang.name].tolist():
      condition_list.append(label)
      
    return condition_list

  def __get_basic_list__(self,localizer):
    basic = self._commandsDataframe[self._commandsDataframe["type"] == "command_basic_move_list"]
    basic_list = basic[localizer.lang.name].tolist()

    basic = self._commandsDataframe[self._commandsDataframe["type"] == "command_basic_move"]
    for label in basic[localizer.lang.name].tolist():
      basic_list.append(label)
      
    return basic_list

  def __get_special_list__(self,localizer):
    special = self._commandsDataframe[self._commandsDataframe["type"] == "command_special_move_list"]
    special_list = special[localizer.lang.name].tolist()

    special = self._commandsDataframe[self._commandsDataframe["type"] == "command_special_move"]
    for label in special[localizer.lang.name].tolist():
      special_list.append(label)
      
    return special_list

  def __get_playbook_list__(self,localizer):
    playbook = self._commandsDataframe[self._commandsDataframe["type"] == "command_playbook_list"]
    playbook_list = playbook[localizer.lang.name].tolist()

    playbook = self._commandsDataframe[self._commandsDataframe["type"] == "command_playbook"]
    for label in playbook[localizer.lang.name].tolist():
      playbook_list.append(label)
      
    return playbook_list

  def get_command(self, localizer, key):
    return self.dictionary[key][localizer.lang.name]
