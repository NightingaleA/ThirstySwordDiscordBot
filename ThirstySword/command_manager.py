import discord
from Data.data_manager  import DataManager
class CommandsManager:
  def __init__(self):
    self.data_manager = DataManager()
   
 
  def get_message_to_send(self, message):
    is_command = self.data_manager.set_language_from_command(message.content)
    if(is_command):
      type = self.data_manager.get_command_type(message.content)

      if(type == self.data_manager.COMMAND_TYPE.command_help_list.name):
        response = self.data_manager.commands.get_list(self.data_manager.localizer,message)
        return response

      if(type == self.data_manager.COMMAND_TYPE.command_basic_move_list.name):
        response = self.data_manager.moves.get_list(self.data_manager.COMMAND_TYPE.command_basic_move,self.data_manager,message)
        return response

      embed=discord.Embed(title=type, color=0xFF5733)
      return embed