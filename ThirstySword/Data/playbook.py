from Utils.text_formatter import Text_Formatter
import discord

class Playbook:
  def __init__(self, id, command, name, blurb, truths, source):
    self.formatter = Text_Formatter()
    self.id = id
    self.command = command
    self.name = name
    self.blurb = blurb
    self.truths = truths
    self.source = source

  def parse_playbook(self, data_manager, message):
    title = data_manager.localizer.get_move_with_key(self.title)
    response = data_manager.localizer.get_move_with_key(self.blurb) + self.formatter.newline
    response = response + self.formatter.newline + self.formatter.newline
    response = response + data_manager.localizer.get_move_with_key(self.truths)

    move_list = self.data_manager.commands_manager
    
    embed = discord.Embed(title=title, colour=5450873, description = response)
    author = message.author
    embed.set_author(name=author.display_name)
    embed.set_thumbnail(url=author.avatar)
    
    return embed