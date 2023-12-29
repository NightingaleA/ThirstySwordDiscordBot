import os
import discord
from discord import app_commands
from input_handler import input_handler
from Managers.slash_command_manager import Slash_Command_Manager
from Localization.localizer import Discord_Translator

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(command_prefix='$', intents=intents)
tree = app_commands.CommandTree(client)
guild = discord.Object(id=725129870174322688)

input = input_handler()
slash = Slash_Command_Manager(tree, input)

@client.event
async def on_ready():
  await tree.set_translator(Discord_Translator(input.data_manager))
  #tree.copy_global_to(guild=guild)
  #tree.clear_commands(guild=None)
  await  tree.sync()
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='$help $ayuda'))

  print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$'):
    response = input.get_response(message.content, message.author.display_name, message.author.display_avatar, message.guild.name)
    await message.channel.send(embed=response)

client.run(TOKEN)