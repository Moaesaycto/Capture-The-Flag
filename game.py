import json, shutil
from time import sleep
import arena, discord

GAME_PATH = "resources/game.json"
CONTROLLER_PATH = "resources/controller.json"
PLAYERS_PATH = 'resources/players.json'
SESSION_KEY_PATH = "resources/session_keys.json"
CLEAN_MAP_PATH = "static/media/clean_map.png"
DISPLAY_MAP_PATH = "static/media/display_map.png"

def start():
    with open(CONTROLLER_PATH, 'r') as fp: init_data = json.load(fp)
    if init_data['time'] == 0: next_section()
    shutil.copyfile(CLEAN_MAP_PATH, DISPLAY_MAP_PATH)
    play()


def play():
    with open(CONTROLLER_PATH, 'r') as fp:
        init_data = json.load(fp)
        init_data['paused'], init_data['stopped'] = False, False
        paused, stopped = init_data['paused'], init_data['stopped']

    with open(CONTROLLER_PATH, 'w') as fp: json.dump(init_data, fp)

    while not paused and not stopped:
        with open(CONTROLLER_PATH, 'r') as fp:
            sleep(1)
            data = json.load(fp)
            state, paused, c_time, stopped = data['state'], data['paused'], data['time'], data['stopped']
            if state == "idle": break
            c_time -= 1
            
            if c_time == 0:
                next_section()
                continue
            
        with open(CONTROLLER_PATH, 'w') as fp:
            data['time'] = c_time
            json.dump(data, fp)

        if state == "commando" and c_time == 10: pause()
            

def next_section():
    with open(GAME_PATH, 'r') as fp:
        game_data = json.load(fp)

    with open(CONTROLLER_PATH, 'r') as fp:
        data = json.load(fp)
        state = data['state']
    
        if state == "idle":
            data['time'] = game_data['grace_period_time']
            data['state'] = "grace"
        
        elif state == "grace":
            if not game_data['orange_flag_placed'] or not game_data['yellow_flag_placed']:
                data['time'] += 60
                discord.global_flag_error()
            
            else:
                data['time'] = game_data['commando_period_time']
                data['state'] = "commando"
                discord.global_commando()
        
        elif state == "commando":
            data['time'] = game_data['informed_period_time']
            data['state'] = "informed"
            arena.generate_flag_map()
            discord.global_informed()
        
        elif state == "informed":
            data['time'] = 0
            data['state'] = "idle"
            data['stopped'] = True
            discord.global_end_draw()
            shutil.copyfile(CLEAN_MAP_PATH, DISPLAY_MAP_PATH)

    with open(CONTROLLER_PATH, 'w') as fp: json.dump(data, fp)


def prev_section():
    with open(GAME_PATH, 'r') as fp:
        game_data = json.load(fp)

    with open(CONTROLLER_PATH, 'r') as fp:
        data = json.load(fp)
        state = data['state']
    
        if state == "commando":
            data['time'] = game_data['grace_period_time']
            data['state'] = "grace"
        
        elif state == "informed":
            data['time'] = game_data['commando_period_time']
            data['state'] = "commando"
        
        elif state == "idle":
            data['time'] = game_data['informed_period_time']
            data['state'] = "informed"
        
        elif state == "grace":
            data['time'] = 0
            data['state'] = "idle"
            data['stopped'] = True
            shutil.copyfile(CLEAN_MAP_PATH, DISPLAY_MAP_PATH)

    with open(CONTROLLER_PATH, 'w') as fp: json.dump(data, fp)


def restart_section():
    with open(GAME_PATH, 'r') as fp:
        game_data = json.load(fp)

    with open(CONTROLLER_PATH, 'r') as fp:
        data = json.load(fp)
        state = data['state']
    
        if state == "grace":
            data['time'] = game_data['grace_period_time']
            data['state'] = "grace"
        
        elif state == "commando":
            data['time'] = game_data['commando_period_time']
            data['state'] = "commando"
        
        elif state == "informed":
            data['time'] = game_data['informed_period_time']
            data['state'] = "informed"

    with open(CONTROLLER_PATH, 'w') as fp: json.dump(data, fp)


def pause():
    with open(CONTROLLER_PATH, 'r') as fp:
        data = json.load(fp)
        data['paused'] = True

    with open(CONTROLLER_PATH, 'w') as fp: json.dump(data, fp)


def add_five():
    with open(CONTROLLER_PATH, 'r') as fp:
        data = json.load(fp)
        data['time'] += 300

    with open(CONTROLLER_PATH, 'w') as fp: json.dump(data, fp)


def restart():
    with open(CONTROLLER_PATH, 'w') as fp: json.dump({"time": 0, "state": "idle", "paused": False, "stopped": True}, fp)


def info():
    with open(CONTROLLER_PATH, 'r') as fp: return json.load(fp)


def get_stats():
    with open(GAME_PATH, 'r') as fp: data = json.load(fp)    
    return data


def set_stats(new_stats):
    with open(GAME_PATH, 'r') as fp: data = json.load(fp)    
    data['grace_period_time'] = new_stats['grace_period_time']
    data['commando_period_time'] = new_stats['commando_period_time']
    data['informed_period_time'] = new_stats['informed_period_time']
    with open(GAME_PATH, 'w') as fp: json.dump(data, fp)

"""
Update game stats
"""
def game_update(stats):
    with open(GAME_PATH, 'r') as fp:
        data = json.load(fp)
        for key in stats: data[key] = stats[key]
    
    with open(GAME_PATH, 'w') as fp: json.dump(data, fp)


def game_reset():
    with open(GAME_PATH, 'w') as fp:
        json.dump({
            "grace_period_time": 600,
            "commando_period_time": 1800,
            "informed_period_time": 1200,
            "default_grace_period_time": 600,
            "default_commando_period_time": 1800,
            "default_informed_period_time": 1200,
            "orange_flag_position": {"x": 1068, "y": 990},
            "yellow_flag_position": {"x": 353, "y": 1442},
            "orange_flag_placed": False,
            "yellow_flag_placed": False
        }, fp)
    
    with open(CONTROLLER_PATH, 'w') as fp:
        json.dump({"time": 0, "state": "idle", "paused": False, "stopped": True}, fp)
    
    with open(PLAYERS_PATH, 'w') as fp:
        json.dump({}, fp)
        
    with open(SESSION_KEY_PATH, 'w') as fp:
        json.dump({"invalid_keys": []}, fp)

if __name__ == '__main__':
    start()