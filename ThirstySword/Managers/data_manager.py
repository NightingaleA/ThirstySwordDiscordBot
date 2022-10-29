import discord
import re

from Managers.commands_manager import Commands_Manager
from Managers.moves_manager import Moves_Manager
from Managers.playbooks_manager import Playbooks_Manager
from Localization.localizer import Localizer
from enum import Enum
from Data.command import Command

class DataManager:
  COMMAND_TYPE = Enum('COMMAND_TYPE', 'command_help_list command_label_list command_label command_condition_list command_condition command_basic_move_list command_basic_move command_special_move_list command_special_move command_playbook_list command_playbook command_playbook_move command_basic_move_extended')
  
  def __init__(self):
    self.commands_manager = Commands_Manager()
    self.localizer = Localizer()
    self.moves_manager = Moves_Manager()
    self.playbooks_manager = Playbooks_Manager()
    self.current_command = None

  def message_contains_command(self, message):
    messageText = message
    messageText = messageText.lower()
    messageText = messageText.replace(" ", "");
    messageText = re.sub('[$]', '', messageText)
    messageText = re.sub(r'<.+?>', '', messageText)
    list_mod = re.findall(r'[-+]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?', messageText)
    messageText = re.sub(r'[-+]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?', '', messageText)

    if not list_mod:
       mod = 0
    else:
      mod = int(list_mod[0] )
      
    self.current_command = self.__get_command_in_message__(messageText)
  
    if(self.current_command != None):
      self.localizer.lang = self.current_command.active_language
      self.current_command.modifier = mod
      return True

    return False      
  
  def __get_command_in_message__(self, text_command):
    command_in_message = None
    
    for command in self.commands_manager.list:     
      if(command.languages[self.localizer.LANGUAGES.english.name ] == text_command):
        command_in_message = Command( command.id, command.languages['english'], command.languages['español'],command.type, command.status)
        command_in_message.active_language = self.localizer.LANGUAGES.english  
        return command_in_message
      if(command.languages[self.localizer.LANGUAGES.español.name] == text_command):
        command_in_message = Command( command.id, command.languages['english'], command.languages['español'],command.type, command.status)
        command_in_message.active_language = self.localizer.LANGUAGES.español  
        return command_in_message
    return command_in_message

  def parse_label(self, message):
    title = self.localizer.get_utils_with_key('asking_for') +  self.localizer.get_label_with_key("title_" + self.current_command.id)
    blurb = self.localizer.get_label_with_key("blurb_" + self.current_command.id)
    
    embed = discord.Embed(title=title, colour=5450873, description = blurb)
    author = message.author
    embed.set_author(name=author.display_name)
    embed.set_thumbnail(url=author.avatar)

    return embed

  def parse_condition(self, message):
    title = self.localizer.get_utils_with_key('asking_for') +  self.localizer.get_condition_with_key("title_" + self.current_command.id)
    blurb = self.localizer.get_condition_with_key("blurb_" + self.current_command.id)
    
    embed = discord.Embed(title=title, colour=5450873, description = blurb)
    author = message.author
    embed.set_author(name=author.display_name)
    embed.set_thumbnail(url=author.avatar)

    return embed
  

    
      

    
