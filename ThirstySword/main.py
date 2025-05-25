import os
import discord
import logging
from discord import app_commands
from input_handler import input_handler
from Managers.slash_command_manager import Slash_Command_Manager
from Localization.localizer import Discord_Translator

TOKEN = os.getenv('DISCORD_TOKEN')
TESTING_GUIld = os.getenv('TESTING_GUILD')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(command_prefix='$', intents=intents)
tree = app_commands.CommandTree(client)
guild = discord.Object(id=TESTING_GUIld)

input = input_handler(client)
slash = Slash_Command_Manager(tree, input)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(" THIRSTY-SWORD ")


@client.event
async def on_ready():
  await tree.set_translator(Discord_Translator(input.data_manager))
  #tree.clear_commands(guild=guild)
  #tree.copy_global_to(guild=guild)
  await  tree.sync()
  await client.change_presence(activity=discord.Activity(
    type=discord.ActivityType.listening, name='$help $ayuda'))

  game = discord.Game(f"Playing Thirsty Sword Lesbians in {len(client.guilds)} servers!")
  await client.change_presence(status=discord.Status.online, activity=game)

  for server in client.guilds:
    client_messages_in_server = []

    for channel in server.channels:
      try:
        messages = [post async for post in channel.history(limit=5)]   
        for message in messages:
          if(message.author == client.user):
            client_messages_in_server.append(message.created_at)
      except:
        continue
      
    client_messages_in_server.sort()
    logger.info("   ")
    if(len(client_messages_in_server)>0):
      logger.info(server.name + ": " + str(client_messages_in_server[0]))
    else:
      logger.info(server.name)

  logger.info("   ")
  logger.info(f'We have logged in as {client.user} with presence in {len(client.guilds)} servers') 


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$'):
    response =await input.get_response(message.content, message.author.display_name, message.author.display_avatar, message.guild.name)
    await message.channel.send(embed=response)

@client.event
async def on_guild_join(guild):
  game = discord.Game(f"Playing Masks in {len(client.guilds)} servers!")
  await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_guild_remove(guild):
  game = discord.Game(f"Playing Masks in {len(client.guilds)} servers!")
  await client.change_presence(status=discord.Status.online, activity=game)

client.run(TOKEN)
