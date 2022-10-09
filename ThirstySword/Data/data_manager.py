from Data.commands_data import Commands
from Data.moves_data import Moves
from Localization.localizer import Localizer
from enum import Enum

class DataManager:
  COMMAND_TYPE = Enum('COMMAND_TYPE', 'command_help_list command_label_list command_label command_condition_list command_condition command_basic_move_list command_basic_move command_special_move_list command_special_move command_playbook_list command_playbook playbook_move')
  
  def __init__(self):
    self.commands = Commands()
    self.localizer = Localizer()
    self.moves = Moves()
  
  def set_language_from_command(self,message):
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
    
