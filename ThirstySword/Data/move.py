import re
import random
import discord
from Utils.text_formatter import Text_Formatter


class Move:

  def __init__(self, id, command, name, trigger, blurb, rolls, type):
    self.formatter = Text_Formatter()
    self.id = id
    self.command = command
    self.name = name
    self.trigger = trigger
    self.blurb = blurb
    self.rolls = rolls
    self.type = type

  def parse_move(self, data_manager):
    response = self.formatter.newline
    title = ''
    response = data_manager.localizer.get_move_with_key(self.blurb) + self.formatter.newline
    
    if (self.rolls == True):
      title = data_manager.localizer.get_utils_with_key("rolled")
      result, die1, die2, mod = self.roll(data_manager.current_command.modifier)
      formatted_result = die1 + " + " + die2 + mod + " = " + result
      response = response + self.formatter.newline + self.formatter.newline + (self.formatter.bold).format(formatted_result)
    else:
      title = data_manager.localizer.get_utils_with_key("triggered")

    title = title + data_manager.localizer.get_move_with_key(self.name) + self.formatter.newline + self.formatter.newline + data_manager.localizer.get_move_with_key(self.trigger)

    embed = discord.Embed(title=title, colour=5450873, description = response)
    
    embed.set_author(name= data_manager.current_command.user_display_name )
    embed.set_thumbnail(url= data_manager.current_command.avatar)

    return embed

  def roll(self, command_mod):
    die_1 = random.randrange(1, 7)
    die_2 = random.randrange(1, 7)
 
    mod = self.__clamp__(command_mod, -1000, 1000)
    string_mod = " " + str(abs(mod))
    if(mod >= 0):
      string_mod = " +" + string_mod
    else:
       string_mod = " –" + string_mod
      
    result = die_1 + die_2 + mod
    
    return str(result), str(die_1), str( die_2), string_mod

  def __clamp__(self, n, smallest, largest):
    return max(smallest, min(n, largest))
