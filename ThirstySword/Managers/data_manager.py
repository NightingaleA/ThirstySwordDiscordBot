from Managers.commands_manager import Commands_Manager
from Managers.moves_manager import Moves_Manager
from Managers.playbooks_manager import Playbooks_Manager
from Localization.localizer import Localizer
from enum import Enum
from Data.command import Command
class DataManager:
  COMMAND_TYPE = Enum('COMMAND_TYPE', 'command_help_list command_label_list command_label command_condition_list command_condition command_basic_move_list command_basic_move command_special_move_list command_special_move command_playbook_list command_playbook command_playbook_move')
  
  def __init__(self):
    self.commands_manager = Commands_Manager()
    self.localizer = Localizer()
    self.moves_manager = Moves_Manager()
    self.playbooks_manager = Playbooks_Manager()
    self.current_command = None

  def message_contains_command(self, message):
    self.current_command = self.__get_command_in_message__(message.lower())

    if(self.current_command != None):
      self.localizer.lang = self.current_command.active_language
      return True

    return False      
  
  def __get_command_in_message__(self,message):
    command_in_message = None
    
    for command in self.commands_manager.list:     
      if(command.languages[self.localizer.LANGUAGES.english.name ] in message):
        command_in_message = Command( command.id, command.languages['english'], command.languages['español'],command.type, command.status)
        command_in_message.active_language = self.localizer.LANGUAGES.english  
        return command_in_message
      if(command.languages[self.localizer.LANGUAGES.español.name] in message):
        command_in_message = Command( command.id, command.languages['english'], command.languages['español'],command.type, command.status)
        command_in_message.active_language = self.localizer.LANGUAGES.español  
        return command_in_message
    return command_in_message

    
      

    
