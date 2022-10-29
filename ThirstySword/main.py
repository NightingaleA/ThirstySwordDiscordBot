import os
import discord
from discord.ext import commands
from Utils.keep_bot_alive import keep_bot_alive
from input_handler import input_handler

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

input = input_handler()


@bot.event
async def on_ready():
  print(f'We have logged in as {bot.user}')


@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  if message.content.startswith('$'):
    response = input.get_message_to_send(message)
    if (response == None):
      response = discord.Embed(
        title=input.data_manager.localizer.get_utils_with_key(
          "ups_title"),
        color=0xFF5733, description=input.data_manager.localizer.get_utils_with_key(
          "ups"))

    await message.channel.send(embed=response)


keep_bot_alive()
bot.run(TOKEN)
