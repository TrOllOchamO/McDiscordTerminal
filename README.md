# McDiscordTerminal
A way to interact with your minecraft server terminal from discord

### How to use it ?

Once installed simply go to your terminal discod channel and type yours commands directly in the chat like this :

![minecraft-step1](./Lib/images/command-minecraft-1.png) ![minecraft-step2](./Lib/images/command-minecraft-1.png)\
![shell-step1](./Lib/images/command-shell-1.png) ![shell-step1](./Lib/images/command-shell-1.png)

#### there is 4 commands :  
``!m [your minecraft command]``\
``!s [your shell command]``\
``!tm`` *simply display the minecraft terminal*\
``!ts`` *simply display the shell terminal*

### How to setup ?

#### 1) Requierments
You must have : 
1. [python](https://www.python.org/), [screen](https://linuxize.com/post/how-to-use-linux-screen/) and [Watchdog](https://github.com/gorakhargosh/watchdog) installed on your server.
2. a discord bot account, if you havn't one yet go to the [discord developper portal](https://discord.com/developers/docs/intro) and [create one](https://discordpy.readthedocs.io/en/stable/discord.html).

#### 2) Download

Theoretically you can download [McDiscordTerminal](https://github.com/TrOllOchamO/McDiscordTerminal) in any directory on your server and it should work fine, though i only tested when the file resided directly in my linux user who host the server.

#### 3) Initilize

To display the terminal in your discord channel [McDiscordTerminal](https://github.com/TrOllOchamO/McDiscordTerminal) simply edit an existing message. That why you will need to fisrt made the bot send the message in your futur discord terminal channel so then he will have a message to edit.\

In order to do that, first you need to edit the ``param.txt`` text file, add the token of your bot and the channel id in witch you want your minecraft terminal. You can check the [param-example.txt](./param-example.txt).\
[Invite your bot](https://discordpy.readthedocs.io/en/stable/discord.html#inviting-your-bot) on your server.\

Run ``initialize-terminal.py``. If you followed the steps before, your bot should send a message in your futur terminal channel.\
![first-bot-message](./Lib/images/initilisation.png)\
Simply copy the id of his message and finish to edit the ``param.txt`` file. You still can check the [param-example.txt](./param-example.txt).\

You are done initilazing !

#### 4) Use

The only thing left to use your bot is to run your minecraft server using the ``run-server.py`` script and after that run ``McDiscordTerminal.py``.