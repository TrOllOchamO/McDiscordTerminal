import os
from Lib.utils import *
from discord.ext import commands, tasks


PATH_TO_PARAM = f'{os.path.realpath(os.path.dirname(__file__))}/param.txt'
PARAM = text2dic(file_path=PATH_TO_PARAM, separator='=')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    channel = bot.get_channel(int(PARAM['id_channel_terminal']))
    await channel.send("""This message is your future terminal ! \nNow you can copy the id of this message into the param.txt file and keep following the tutorial :thumbsup:""")
    print("A message should has been send to your terminal channel")
    await bot.close()

bot.run(PARAM['token'])