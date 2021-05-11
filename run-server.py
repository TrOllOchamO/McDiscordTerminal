import os
from Lib.utils import text2dic

PATH_TO_THIS_DIRECTORY = os.path.realpath(os.path.dirname(__file__))

PATH_TO_PARAM = f'{PATH_TO_THIS_DIRECTORY}/param.txt'
PARAM = text2dic(file_path=PATH_TO_PARAM, separator='=')

PATH_TO_MINECRAFT_TERMINAL_LOG = f'{PATH_TO_THIS_DIRECTORY}/Lib/terminal_minecraft/terminal_minecraft.txt'
PATH_TO_SHELL_TERMINAL_LOG = f'{PATH_TO_THIS_DIRECTORY}/Lib/terminal_shell/terminal_shell.txt'

#deleting last logs so they didn't accumulate
os.system(f'sudo rm -rf {PATH_TO_MINECRAFT_TERMINAL_LOG}')
os.system(f'sudo rm -rf {PATH_TO_SHELL_TERMINAL_LOG}')

#starting the server inside a dedicated screen
os.system(f"sudo -u {PARAM['user_name']} screen -dmS {PARAM['screen_minecraft_session_name']} -L -Logfile {PATH_TO_MINECRAFT_TERMINAL_LOG}")
os.system(f"sudo -u {PARAM['user_name']} screen -S {PARAM['screen_minecraft_session_name']} -X stuff 'cd {PARAM['path_to_your_minecraft_server_file']} && {PARAM['server_start_command']}^M'")

#starting the shell inside an other screen
os.system(f"sudo -u {PARAM['user_name']} screen -dmS {PARAM['screen_shell_session_name']} -L -Logfile {PATH_TO_SHELL_TERMINAL_LOG}")
