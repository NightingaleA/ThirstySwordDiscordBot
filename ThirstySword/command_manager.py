import discord
from Data.data_manager  import DataManager
class CommandsManager:
  def __init__(self):
    self.data_manager = DataManager()
   
 
  def get_message_to_send(self, message):
    self.is_command = self.data_manager.set_command_language(message.content)
    if(self.is_command):
      self.type = self.data_manager.get_command_type(message.content)

      if(self.type == self.data_manager.COMMAND_TYPE.help_list.name):
        response = self.data_manager.commands.get_list(self.data_manager.localizer.lang,message)
        return response
        
      return self.type