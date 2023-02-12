import eel
import os
import json
from filedialogs import open_folder_dialog
import subprocess


# Set web files folder
eel.init('ui')

dolphin_exe_path = 'C:/Program Files/Dolphin-x64/Dolphin.exe'
assets_dir = 'data/assets/'
games = {}

def sort_games(games_dict):
    sorted_games = {}
    # sort the games by "last-played" in unix time
    sorted_games = sorted(games_dict.items(), key=lambda x: x[1]['last-played'], reverse=True)
    # convert the list of tuples to a dictionary
    sorted_games = dict(sorted_games)
    return sorted_games
    

@eel.expose
def get_games():
    # get the games object from data/user.json
    with open('data/user.json') as f:
        data = json.load(f)
        games = data['games']
        games = sort_games(games)
        return games

@eel.expose
def get_default_game_dir():
    # get the current directory
    current_dir = os.getcwd()
    current_dir += '/data/assets/'
    return current_dir

@eel.expose
def get_folder_dialog():
    # open the folder dialog and return the path
    dir = open_folder_dialog()
    if dir:
        return dir
    else:
        return get_default_game_dir()


def check_if_first_launch():
    # check if the user.json file exists
    if not os.path.exists('data/user.json'):
        return True
    else:
        return False

def create_user_json():
    # create the user.json file
    with open('data/user.json', 'w') as f:
        json.dump({}, f)

def set_game_dir(dir):
    # set the game directory in the user.json file
    if not os.path.exists('data/user.json'):
        create_user_json()
    with open('data/user.json') as f:
        data = json.load(f)
        data['game-dir'] = dir
    with open('data/user.json', 'w') as f:
        json.dump(data, f)

def get_assets_dir():
    # get the game directory from the user.json file
    with open('data/user.json') as f:
        data = json.load(f)
        dir = data['assets-dir']
        # if the directory is relative, make it absolute
        if not os.path.isabs(dir):
            dir = os.path.abspath(dir)
        # make sure it ends with a slash
        if not dir.endswith('/'):
            dir += '/'
        return dir


@eel.expose
def launch(uid):
    for game in games:
        # get the key of each game
        if game == uid:
            open_dolphin('-e ' + get_assets_dir() + uid + 'build/DATA/sys/main.dol')

def open_dolphin(args):
    # open dolphin with the given arguments
    subprocess.Popen([dolphin_exe_path, args])


def main():
    # check if it is the first launch
    if check_if_first_launch():
        # if it is the first launch, open the setup page with no resize
        eel.start('setup.html', size=(500, 500))
    else:
        ##games = get_games()
        #launch("001")
        #"C:\Program Files\Dolphin-x64\Dolphin.exe"
        #subprocess.Popen(["C:/Program Files/Dolphin-x64/Dolphin.exe", "-e C:/Users/thise/source/repos/EpicMickeyToolboxLite/data/assets/games/001/build/DATA/sys/main.dol"])
        # do the above but with double back slashes
        ##subprocess.Popen(["C:\\Program Files\\Dolphin-x64\\Dolphin.exe", "C:\\\\Users\\thise\\source\\repos\\EpicMickeyToolboxLite\\data\\assets\\games\\001\\build\\DATA\\sys\\main.dol"])
        eel.start('index.html', size=(500, 500))


if __name__ == '__main__':
    main()