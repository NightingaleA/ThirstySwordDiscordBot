from Data.commands_data import Commands
from Localization.localizer import Localizer
from enum import Enum

class DataManager:
  COMMAND_TYPE = Enum('COMMAND_TYPE', 'help_list label_list label condition_list condition basic_move_list basic_move special_move_list special_move playbook_list playbook playbook_move')
  def __init__(self):
    self.commands = Commands()
    self.localizer = Localizer()
  
  def set_command_language(self,message):
    for self.command in self.commands.list:     
      if(self.command.english in message):
        self.localizer.lang = self.localizer.LANGUAGES.english  
        return True
      if(self.command.español in message):
        self.localizer.lang = self.localizer.LANGUAGES.español
        return True
    return False
      
  def get_command_type(self, command):
    for self.command in self.commands.list:
      if(self.localizer.lang == self.localizer.LANGUAGES.english):
        if(self.command.english in command):
          return self.command.type
      if(self.localizer.lang == self.localizer.LANGUAGES.español):
        if(self.command.español in command):
          return self.command.type
    
