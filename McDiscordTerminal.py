#--------------------------------------------------------Imports----------------------------------------------------#

import os
from Lib.utils import *
from discord.ext import commands, tasks
from Lib.hachiko.hachiko import AIOWatchdog, AIOEventHandler

#--------------------------------------------------------Classes-----------------------------------------------------#

class Terminal():

    def __init__(self, path_to_log, channel_id, message_id, bot):
        self.path_to_log = path_to_log
        self.channel_id = channel_id
        self.message_id = message_id
        self.bot = bot

    async def send_message(self, message, bot=None, channel_id=None):
        if channel_id is None: channel_id = self.channel_id
        await bot.wait_until_ready()
        channel = bot.get_channel(int(channel_id))
        await channel.send(message)

    async def edit_message(self, message, bot=None, channel_id=None, message_id=None):
        if bot is None: bot = self.bot
        if channel_id is None: channel_id = self.channel_id
        if message_id is None: message_id = self.message_id

        await bot.wait_until_ready()
        channel = bot.get_channel(int(channel_id))
        msg = await channel.fetch_message(int(message_id))
        await msg.edit(content=message)

    async def send_terminal(self, bot=None, channel_id=None, message_id=None, path_to_log=None):
        if bot is None: bot = self.bot
        if channel_id is None: channel_id = self.channel_id
        if message_id is None: message_id = self.message_id
        if path_to_log is None: path_to_log = self.path_to_log

        lastest_lignes_terminal = getLastestLines(file_path=path_to_log, number_of_lines=15)
        msg = f"""```\n{lastest_lignes_terminal}```"""
        await self.edit_message(message=msg, bot=bot, channel_id=channel_id, message_id=message_id)


class Event_handeler_minecraft(AIOEventHandler):

    async def on_modified(self, event):
        if choosen_terminal.selected == 'minecraft':
            await terminal_minecraft.send_terminal()
            print('Modified minecraft')


class Event_handeler_shell(AIOEventHandler):

    async def on_modified(self, event):
        if choosen_terminal.selected == 'shell':
            await terminal_shell.send_terminal()
            print('Modified shell')


class Used_terminal():

    selected = 'minecraft'

    def change_to_minecraft(self):
        self.selected = 'minecraft'

    def change_to_shell(self):
        self.selected = 'shell'

#--------------------------------------------Creating const and objects----------------------------------------------#

# extract the param from the param file
PATH_TO_PARAM = f'{os.path.realpath(os.path.dirname(__file__))}/param.txt'
PARAM = text2dic(file_path=PATH_TO_PARAM, separator='=')

# seting the way to trigger the bot
bot = commands.Bot(command_prefix='!')


terminal_minecraft = Terminal(path_to_log=f'{os.path.realpath(os.path.dirname(__file__))}/Lib/terminal_minecraft/terminal_minecraft.txt',
                              channel_id=PARAM['id_channel_terminal'],
                              message_id=PARAM['id_message_terminal'],
                              bot=bot)

terminal_shell = Terminal(path_to_log=f'{os.path.realpath(os.path.dirname(__file__))}/Lib/terminal_shell/terminal_shell.txt',
                          channel_id=PARAM['id_channel_terminal'],
                          message_id=PARAM['id_message_terminal'],
                          bot=bot)

# creating terminal selector
choosen_terminal = Used_terminal()

# creating handelers
event_handeler_minecraft = Event_handeler_minecraft()
event_handeler_shell = Event_handeler_shell()

# creation and starting handeler for minecraft
observer_minecraft = AIOWatchdog(event_handler=event_handeler_minecraft,
                                 path=f'{os.path.realpath(os.path.dirname(__file__))}/Lib/terminal_minecraft/',
                                 recursive=True)
observer_minecraft.start()

# creation and starting handeler for shell
observer_shell = AIOWatchdog(event_handler=event_handeler_shell,
                             path=f'{os.path.realpath(os.path.dirname(__file__))}/Lib/terminal_shell/',
                             recursive=True)
observer_shell.start()

#-------------------------------------------------Terminals commands-------------------------------------------------#

@bot.event
async def on_ready():
    print("Terminal Discord is ready !")
    commande = rf"""sudo -u {PARAM['user_name']} screen -S {PARAM['screen_shell_session_name']} -X stuff 'cd ~^M'"""
    os.system(commande)


@bot.command(name='m')
async def commande_minecraft(ctx, *, commande_minecraft=''):
    try:
        if str(ctx.channel) == "terminal":
            await ctx.message.delete()
            choosen_terminal.change_to_minecraft()

            # executing the command in the minecraft screen
            commande = rf"""sudo -u {PARAM['user_name']} screen -S {PARAM['screen_minecraft_session_name']} -X stuff '{commande_minecraft}^M'"""
            os.system(commande)
    except:
        print('a problem has occurred while trying to send the commend to the minecraft terminal')


@bot.command(name='s')
async def commande_shell(ctx, *, commande_shell=''):
    try:
        if str(ctx.channel) == "terminal":
            await ctx.message.delete()
            choosen_terminal.change_to_shell()

            # executing the command in the shell screen
            commande = rf"""sudo -u {PARAM['user_name']} screen -S {PARAM['screen_shell_session_name']} -X stuff '{commande_shell}^M'"""
            os.system(commande)
    except:
        print('a problem has occurred while trying to send the commend to the shell terminal')


@bot.command(name='tm')
async def show_minecraft_teminal(ctx):
    try:
        if str(ctx.channel) == "terminal":
            await ctx.message.delete()
            choosen_terminal.change_to_minecraft()
            await terminal_minecraft.send_terminal()
            print('the minecraft terminal as been successfully display')
    except:
        print("a problem has occurred while trying to display the minecraft terminal")


@bot.command(name='ts')
async def show_shell_teminal(ctx):
    try:
        if str(ctx.channel) == "terminal":
            await ctx.message.delete()
            choosen_terminal.change_to_shell()
            await terminal_shell.send_terminal()
            print('the shell terminal as been successfully display')
    except:
        print("a problem has occurred while trying to display the shell terminal")


@tasks.loop(seconds=30)
async def loop_terminals():
    await bot.wait_until_ready()
    if bot.is_closed():
        observer_minecraft.stop()
        observer_minecraft.join()
        observer_shell.stop()
        observer_shell.join()

#--------------------------------------------------Starting loops----------------------------------------------------#

loop_terminals.start()
bot.run(PARAM['token'])
