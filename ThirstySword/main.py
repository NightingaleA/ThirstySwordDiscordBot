import os
import discord
from discord.ext import commands
from Utils.keep_bot_alive import keep_bot_alive
from command_manager import CommandsManager

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

commands_manager = CommandsManager()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$'):
        response = commands_manager.get_message_to_send(message)
        await message.channel.send(embed =response)

keep_bot_alive()
bot.run(TOKEN)
